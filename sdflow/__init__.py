# sdui_core/__init__.py
from .components import container, text, input, button, markdown, link


__all__ = ["HTMLRenderer"]


class HTMLRenderer:
    """
    Native OOP rendering engine for Anobisoft SDUI Framework.
    Encapsulates form state and provides recursive component tree traversal.
    """

    # 1. INITIALIZERS
    def __init__(self, form_data: dict = None):
        """
        Initializes the renderer with an optional form state.
        
        :param form_data: A dictionary containing current input values keyed by their IDs.
        """
        self.form_data = form_data or {}

    # 2. PUBLIC METHODS (PUBLIC API)
    def render(self, sdui_json: dict) -> str:
        """
        Main entry point: transforms the SDUI JSON specification into a clean HTML string.
        
        :param sdui_json: The complete JSON layout structure from the backend.
        :return: A compiled HTML string ready for browser rendering.
        """
        root_node = sdui_json.get("root", {})
        return self._render(root_node)

    # 3. PRIVATE METHODS (INTERNAL RECURSION)
    def _render(self, node: dict) -> str:
        node_type = node.get("type")
        custom_style = node.get("style", "")
        
        if custom_style:
            class_attr = f'class="{custom_style}:sdflow-{node_type}"'
        else:
            class_attr = f'class="sdflow-{node_type}"'

        match node_type:
            case "text":
                return text.render(node, class_attr)
            case "input":
                field_id = node.get("id", "")
                field_value = self.form_data.get(field_id, "")
                return input.render(node, class_attr, value=field_value)
            case "button":
                return button.render(node, class_attr)
            case "markdown":
                return markdown.render(node, class_attr)
            case "link":
                return link.render(node, class_attr)
            case "container":
                return container.render(node, class_attr, self._render)
            case _:
                return ""

