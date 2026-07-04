def render(node: dict, class_attr: str) -> str:
    """
    Renders a standard read-only plain text typography element.
    Supports native multiline text with custom sizing, alignments, and spacings.

    :param node: Dictionary containing the 'value' key with the raw text string.
    :param class_attr: Clean HTML class attribute string from style design tokens.
    :return: A compiled HTML layout snippet for the text block.
    
    Optional JSON params:
    - font_size (int): Typography size in pixels. Default: 16.
    - font_weight (int/str): Text weight (e.g., 500, 700, "bold"). Default: 500.
    - alignment (str): Text horizontal alignment ("left", "center", "right", "justify"). Default: "left".
    - line_height (float): Line spacing scalar. Default: 1.5.
    - margin_bottom (int): Space below the element in pixels. Default: 12.
    - color (str): Hex or CSS text color code. Default: "inherit".
    """
    font_size = node.get("font_size", 16)
    font_weight = node.get("font_weight", 500)
    alignment = node.get("alignment", "left")
    line_height = node.get("line_height", 1.5)
    margin_bottom = node.get("margin_bottom", 12)
    color = node.get("color", "inherit")
    
    return (
        f'<div {class_attr} style="'
        f'font-size: {font_size}px; '
        f'font-weight: {font_weight}; '
        f'text-align: {alignment}; '
        f'line-height: {line_height}; '
        f'margin-bottom: {margin_bottom}px; '
        f'color: {color}; '
        f'white-space: pre-line; '
        f'display: block;'
        f'">{node["value"]}</div>'
    )
