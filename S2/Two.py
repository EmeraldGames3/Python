def html_tag(tag: str, s: str) -> str:
    tag1 = '<' + tag + '> '
    tag2 = ' </' + tag + '>'
    new_s = tag1 + s + tag2
    return new_s


print(html_tag('i', 'Python'))
