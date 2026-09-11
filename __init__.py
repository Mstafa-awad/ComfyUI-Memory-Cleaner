"""Safe RAM/VRAM cleaner gate for ANY socket type.

Frees GPU model memory and Python garbage WITHOUT touching ComfyUI's
execution cache, so upstream results (Trellis meshes, quad outputs, ...)
stay cached and changing a widget downstream re-runs only the changed node.

Both inputs are wildcards ("*"): MESH, GLTF/GLB, trimesh objects, IMAGE,
LATENT, or anything else your workflow produces. Whatever enters is
returned unchanged, in the same slot order, after the cleanup runs.

Deliberately NOT used here (these are what destroyed the cache before):
  * comfy.memory_management.extra_ram_release(..., free_active=True)
  * prompt_queue.set_flag("free_memory", True)
Both evict cached node outputs and force full re-runs from Trellis.
"""
import gc
import time

try:
    import torch
except Exception:
    torch = None

try:
    import comfy.model_management as mm
except Exception:
    mm = None


class MemoryCleaner:
    """Pass-through memory-clean gate for any two sockets."""

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "optional": {
                "input_1": ("*",),
                "input_2": ("*",),
                "enabled": ("BOOLEAN", {"default": True}),
                "always_run": ("BOOLEAN", {"default": True}),
                "clean_vram": ("BOOLEAN", {"default": True}),
                "clean_ram": ("BOOLEAN", {"default": True}),
            },
        }

    RETURN_TYPES = ("*", "*")
    RETURN_NAMES = ("output_1", "output_2")
    FUNCTION = "clean_and_pass"
    CATEGORY = "mesh/utils"
    OUTPUT_NODE = False
    DESCRIPTION = (
        "Frees VRAM (unloads ComfyUI models + empties the CUDA allocator) and RAM "
        "(Python garbage collection) without evicting ComfyUI's execution cache. "
        "Accepts ANY socket type (MESH, GLB/GLTF, trimesh, IMAGE, LATENT, ...) on "
        "both inputs and passes them through unchanged, in the same slot order. "
        "Place it right after generation and before the heavy mesh nodes."
    )

    @classmethod
    def IS_CHANGED(cls, **kwargs):
        """Re-run the cleaning side effect every prompt when always_run is on.

        Safe for caching: the node returns the exact same objects, so
        downstream cache keys (input objects + widget values) stay valid and
        downstream nodes are NOT forced to re-execute.
        """
        if kwargs.get("always_run", True):
            return time.time()
        return "cached"

    def clean_and_pass(
        self,
        input_1=None,
        input_2=None,
        enabled=True,
        always_run=True,
        clean_vram=True,
        clean_ram=True,
    ):
        if enabled:
            # 1) Detach models from VRAM. Cache-safe: touches only loaded model
            #    weights, never cached node outputs.
            if clean_vram and mm is not None:
                try:
                    mm.unload_all_models()
                except Exception:
                    pass

            # 2) Python garbage. Cache-safe: cached outputs are still referenced
            #    by the execution cache, so gc cannot free them.
            if clean_ram:
                gc.collect()

            # 3) Return freed CUDA blocks to the driver.
            if clean_vram and torch is not None and torch.cuda.is_available():
                try:
                    torch.cuda.synchronize()
                except Exception:
                    pass
                try:
                    if mm is not None and hasattr(mm, "soft_empty_cache"):
                        mm.soft_empty_cache()
                    else:
                        torch.cuda.empty_cache()
                except Exception:
                    pass

        # Exact same objects out: no copy, no modification, same slot order.
        return (input_1, input_2)


NODE_CLASS_MAPPINGS = {
    "MemoryCleaner": MemoryCleaner,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "MemoryCleaner": "VRAM/RAM Cleaner (Any-Type Passthrough)",
}