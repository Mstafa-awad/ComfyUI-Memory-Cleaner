# ComfyUI-Memory-Cleaner

A cache-safe RAM/VRAM cleanup gate for ComfyUI workflows.


# 🚀 SUPPORT MOSTAADTECH

### ❤️ Enjoying this project / workflow?

I’m **MostAadTech**, I create FREE ComfyUI workflows, local AI tools, 3D pipelines, and open-source projects.

If this project or workflow helped you, **please consider following me or supporting my work**. It helps me keep building, testing, and releasing more free tools and workflows.

---

## 💜 Support Me on Patreon

👉 **[Support MostAadTech on Patreon](https://www.patreon.com/cw/MostafaAwad/membership)**

Your support helps me spend more time developing **FREE AI tools, ComfyUI workflows, and 3D pipelines**.

---

## 🌐 Follow MostAadTech

* ▶️ **[YouTube](https://www.youtube.com/@MostAadTech)** — Tutorials, workflows & AI projects
* 📸 **[Instagram](https://www.instagram.com/mostaadtech/)** — Projects, updates & behind the scenes
* 𝕏 **[X / Twitter](https://x.com/MostAadTech)** — Updates, releases & experiments
* 💻 **[GitHub](https://github.com/Mstafa-awad)** — Open-source projects & code

---

### ⭐ One Follow Helps

**Follow • Star • Share • Support**

Every follow, GitHub star, share, and Patreon supporter helps me continue making **FREE tools for the AI community.**

**Thank you for supporting MostAadTech! ❤️**


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
