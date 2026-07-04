def render(node: dict, class_attr: str) -> str:
    """
    Renders a standard inline semantic text link.

    :param node: Dictionary containing text, target, and optional design variables.
    :param class_attr: CSS class string from style design tokens.
    :return: A compiled HTML anchor tag string.
    """
    target = node.get("target", "#")
    font_size = node.get("font_size", 14)
    margin_top = node.get("margin_top", 0)
    color = node.get("color", "#007bff")
    
    return (
        f'<a {class_attr} href="{target}" style="'
        f'color: {color}; '
        f'text-decoration: none; '
        f'font-size: {font_size}px; '
        f'margin-top: {margin_top}px; '
        f'display: inline-block;'
        f'">{node["text"]}</a>'
    )
