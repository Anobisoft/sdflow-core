import markdown

def render(node: dict, class_attr: str) -> str:
    html_content = markdown.markdown(node.get("value", ""), extensions=["nl2br"])
    return (
        f'<div {class_attr} style="font-size:15px; '
        f'line-height:1.6; color:#333; margin-bottom:16px;">'
        f'{html_content}</div>'
    )
