def render(node: dict, class_attr: str, value: str = "") -> str:
    """
    Renders an interactive native HTML5 form input field.
    Handles data types, validation, auto-completion, and fully customizable geometry tokens.

    :param node: Dictionary defining field ID, placeholders, behavior, and visual styles.
    :param class_attr: Clean HTML class attribute string from style design tokens.
    :param value: Optional string containing the preserved state value for form reloading.
    :return: A compiled HTML input tag with native form auto-fill support.
    
    Optional JSON params:
    - input_type (str): Native field validation type (e.g., "text", "email", "number"). Default: "text".
    - is_password (bool): If True, masks the input character stream. Default: False.
    - autocomplete (str): Native HTML auto-fill hint (e.g., "username", "new-password"). Default: "".
    - padding (int): Internal text spacing clearance in pixels. Default: 10.
    - border_width (int): Outline frame stroke thickness in pixels. Default: 1.
    - border_color (str): Hex outline frame boundary color. Default: "#ccc".
    - border_radius (int): Corner roundness geometry radius in pixels. Default: 4.
    - margin_bottom (int): Space below the element layout in pixels. Default: 0.
    """
    is_password = node.get("is_password", False)
    input_type = "password" if is_password else node.get("input_type", "text")
    
    padding = node.get("padding", 10)
    border_width = node.get("border_width", 1)
    border_color = node.get("border_color", "#ccc")
    border_radius = node.get("border_radius", 4)
    margin_bottom = node.get("margin_bottom", 0)
    
    current_value = "" if is_password else value
    value_attr = f'value="{current_value}"' if current_value else ''
    autocomplete_attr = f'autocomplete="{node.get("autocomplete", "")}"' if node.get("autocomplete") else ''
    
    return (
        f'<input {class_attr} type="{input_type}" name="{node["id"]}" '
        f'placeholder="{node["placeholder"]}" {value_attr} {autocomplete_attr} required '
        f'style="'
        f'padding: {padding}px; '
        f'font-size: 14px; '
        f'border: {border_width}px solid {border_color}; '
        f'border-radius: {border_radius}px; '
        f'margin-bottom: {margin_bottom}px; '
        f'width: 100%; '
        f'box-sizing: border-box;'
        f'">'
    )
