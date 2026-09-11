# ComfyUI-Memory-Cleaner

A cache-safe RAM/VRAM cleanup gate for ComfyUI workflows.

## What it does

`VRAM/RAM Cleaner (Any-Type Passthrough)` accepts two wildcard inputs (`*`) and returns the exact same objects in the exact same slot order after cleanup.

It can:

- Unload ComfyUI model weights from VRAM.
- Run Python garbage collection for RAM cleanup.
- Release cached CUDA allocator blocks.
- Leave ComfyUI's execution cache alone.

## Installation

Copy this folder into:

```text
ComfyUI/custom_nodes/ComfyUI-Memory-Cleaner
```

Then restart ComfyUI.

## Dependencies

No third-party Python packages are bundled with this repository.

The node optionally uses:

- ComfyUI's `comfy.model_management` module, supplied by ComfyUI.
- PyTorch (`torch`), supplied by the user's ComfyUI installation.
- Python standard-library modules `gc` and `time`.

## License

This project is licensed under the **GNU General Public License v3.0 or later (GPL-3.0-or-later)**. See `LICENSE`.

Commercial use, modification, and redistribution are permitted subject to the GPL-3.0-or-later terms.

## Third-party software

This repository does not bundle ComfyUI or PyTorch. Their own licenses remain applicable to those separate software components.

ComfyUI is GPL-3.0 licensed by its upstream project:
https://github.com/Comfy-Org/ComfyUI
