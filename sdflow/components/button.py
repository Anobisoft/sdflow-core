def render(node: dict, class_attr: str) -> str:
    """
    Renders an interactive native form submit or action button.
    Provides visual control over typography, background colors, and geometry spacing.

    :param node: Dictionary defining the visible text and the associated action behavior.
    :param class_attr: Clean HTML class attribute string from style design tokens.
    :return: A compiled native HTML button element string.
    
    Optional JSON params:
    - background (str): Hex color for button background. Default: "#007fff".
    - color (str): Hex color for button label text. Default: "white".
    - border_radius (int): Button corner rounding radius in pixels. Default: 4.
    - padding (int): Internal vertical text spacing in pixels. Default: 12.
    - font_size (int): Text label size in pixels. Default: 16.
    - margin_top (int): Top clearance spacing in pixels. Default: 4.
    """
    action = node.get("action", {})
    action_type = action.get("type", "submit")
    
    # Resolve button behavior type for HTML forms
    btn_type = "submit" if action_type == "submit" else "button"
    
    bg_color = node.get("background", "#007fff")
    text_color = node.get("color", "white")
    border_radius = node.get("border_radius", 4)
    padding = node.get("padding", 12)
    margin_top = node.get("margin_top", 4)
    font_size = node.get("font_size", 16)
    
    return (
        f'<button {class_attr} type="{btn_type}" style="'
        f'padding: {padding}px; '
        f'background: {bg_color}; '
        f'color: {text_color}; '
        f'border: none; '
        f'border-radius: {border_radius}px; '
        f'font-size: {font_size}px; '
        f'font-weight: bold; '
        f'margin-top: {margin_top}px; '
        f'width: 100%; '
        f'cursor: pointer;'
        f'">{node["text"]}</button>'
    )
