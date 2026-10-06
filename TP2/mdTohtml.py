import re

def header(txt):
    level = len(txt.group(1))    #quantos '#'
    text = txt.group(2)

    return f"<h{level}>{text}</h{level}>"

def mdTohtml(text):
    #cabeçalhos
    text = re.sub(r'^(#{1,6}) (.*)$', header, text, flags=re.MULTILINE)
    #bold
    text = re.sub(r'\*{2}(.*?)\*{2}', r'<b>\1</b>', text)
    #itálico
    text = re.sub(r'\*(.*?)\*', r'<i>\1</i>', text)
    #listas numeradas
    text = re.sub(r'^\d+\. (.*)$', r'<li>\1</li>', text, flags=re.MULTILINE)
    text = re.sub(r'((?:<li>.*</li>\n?)+)', r'<ol>\n\1</ol>', text)
    #imagens
    text = re.sub(r'!\[(.*?)\]\((.*?)\)', r'<img src="\2" alt="\1"/>', text)
    #links
    text = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', text)

    return text

exemplo = """# Título

Isto é texto **a negrito** e isto é *itálico*.

## Subtítulo

1. Primeiro item
2. Segundo item
3. Terceiro item

Imagem: ![gato](https://cutecats.com/kitten.png)

Link: [gatos fofos](https://cutecats.com)
"""

print(mdTohtml(exemplo))