def render(node: dict, class_attr: str, render_child_func) -> str:
    """
    Renders a structural container element with directional and alignment controls.
    Maps to native web CSS Flexbox rules with fully customizable cross-axis alignment.

    :param node: Dictionary containing element specifications and children.
    :param class_attr: Clean HTML class attribute string from style design tokens.
    :param render_child_func: Reference to the core recursive dispatcher.
    :return: A compiled HTML string enclosing all nested child elements.
    
    Optional JSON params:
    - orientation (str): Layout direction, either "vertical" or "horizontal". Default: "vertical".
    - alignment (str): Cross-axis alignment ("stretch", "baseline", "center", "start", "end"). Default: "stretch".
    - padding (int): Internal padding in pixels. Default: 0.
    - spacing (int): Gap between children in pixels. Default: 12.
    - max_width (int): Maximum container width in pixels. Default: 320.
    """
    orientation = node.get("orientation", "vertical")
    alignment = node.get("alignment", "stretch")
    padding = node.get("padding", 0)
    spacing = node.get("spacing", 12)
    max_width = node.get("max_width", 320)
    
    # Resolving layout direction
    flex_direction = "row" if orientation == "horizontal" else "column"
    
    # Mapping custom alignment tokens to standard web CSS cross-axis alignment rules
    alignment_map = {
        "start": "flex-start",
        "end": "flex-end",
        "center": "center",
        "baseline": "baseline",
        "stretch": "stretch"
    }
    css_align = alignment_map.get(alignment, "stretch")
    
    children_html = "".join(render_child_func(child) for child in node.get("children", []))
    
    return (
        f'<div {class_attr} style="'
        f'display: flex; '
        f'flex-direction: {flex_direction}; '
        f'align-items: {css_align}; '
        f'gap: {spacing}px; '
        f'padding: {padding}px; '
        f'max-width: {max_width}px; '
        f'width: 100%; '
        f'margin: 0 auto;'
        f'">{children_html}</div>'
    )
