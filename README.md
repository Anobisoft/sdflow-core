# Anobisoft sdflow-core 🚀

A lightweight, high-performance, and platform-agnostic **Server-Driven UI/Flow (SDUI)** rendering engine written in Python. 

`sdflow-core` acts as a monolithic source of truth for your UI specifications. It empowers backends to dynamically dictate responsive application layouts, map visual design tokens, and handle state workflows seamlessly across **Web (SSR)**, **iOS (sdflow-ios)**, and **Android (sdflow-android)** platforms without requiring client-side updates.

---

## Key Architectural Principles 💡

*   **Strict OOP Layout Engine:** Core compilation logic is encapsulated entirely inside the dynamic `HTMLRenderer` class, maintaining robust form states and clean execution contexts during deep recursion.
*   **Native `match-case` Dispatching:** Leverages Python's modern structural pattern matching for highly efficient node traversal and minimal runtime memory allocations.
*   **Centralized Class Hooks:** Dynamically stitches style tokens into unified attributes (`class="custom-token sdui-type"`), completely decoupling programmatic layouts from style-sheet implementations.
*   **Multi-Screen Bundling:** Supports multi-page flow delivery (`bundle_id`) to pre-cache workflows and switch UI screens instantly on the client-side at 60 FPS without additional network dispatches.
*   **International Open-Source Standards:** Completely documented in clean English utilizing industry-standard Docstrings for frictionless `Sphinx` / `MkDocs` documentation builds.

---

## Supported Core Components 🧱

The framework provides an initial baseline package containing 6 essential cross-platform components:
1.  `container` — Structural blocks managing directional orientations (`vertical`/`horizontal`) and strict cross-axis alignments (`baseline`, `center`, `stretch`).
2.  `text` — Typography layer supporting responsive text sizing, paragraph weights, custom alignments, and raw multi-line strings (`\n`).
3.  `input` — Form element handling validations, secure fields masking, and automatic HTML5 auto-complete rules.
4.  `button` — Native clickable element driving structural data submissions or platform actions.
5.  `markdown` — Dynamic paragraphs securely converting complex structures (lists, bold styling) into layout nodes with interceptable deep-link schemas (`action://`).
6.  `link` — Independent anchor strings driving lightweight modular standalone navigations.

---

## Installation 📦

Add `sdflow-core` directly from your Git ecosystem repository into your project's `requirements.txt`:

```text
git+https://github.com/anobisoft/sdflow-core.git@release-0.1.0
```

---

## Quick Start (Backend Web SSR Adapter Example) 🛠️

Integrating the core compiler inside a standard `FastAPI` endpoint takes less than a few lines of code:

```python
import json
from fastapi import Request
from fastapi.responses import HTMLResponse
from sdflow_core import HTMLRenderer

async def render_sdui_page(request: Request, sdui_json_spec: dict, inputs_state: dict = None) -> HTMLResponse:
    # 1. Initialize the strict OOP engine with preserved form states
    renderer = HTMLRenderer(form_data=inputs_state)
    
    # 2. Compile the JSON specifications recursively into raw HTML content
    compiled_body = renderer.render(sdui_json_spec)
    
    # 3. Assemble the responsive document frame
    full_html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Anobisoft SDUI Environment</title>
    </head>
    <body>
        <main class="sdflow-viewport-wrapper">
            {compiled_body}
        </main>
    </body>
    </html>
    """
    return HTMLResponse(content=full_html, status_code=200)
```

---

## License 📄

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for more details.
