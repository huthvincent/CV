import re

highlights_to_add = [
    "li2025adversarial",
    "chen2024janus",
    "zhu2022SEAM",
    "zhu2026foundation",
    "zhu2025near"
]

with open("own-bib.bib", "r") as f:
    content = f.read()

# First, remove 'highlight' from everywhere
def remove_highlight(match):
    kws = match.group(1).split(',')
    kws = [k.strip() for k in kws if k.strip() != 'highlight']
    return f"keywords      = {{{', '.join(kws)}}}"

content = re.sub(r'keywords\s*=\s*\{([^\}]+)\}', remove_highlight, content)

# Now, add 'highlight' to the designated entries
def add_highlight(key, text):
    pattern = r'(@[a-zA-Z]+\{'+key+r',[\s\S]*?keywords\s*=\s*\{)([^\}]+)(\})'
    def repl(m):
        kws = [k.strip() for k in m.group(2).split(',')]
        if 'highlight' not in kws:
            kws.insert(0, 'highlight')
        return m.group(1) + ', '.join(kws) + m.group(3)
    return re.sub(pattern, repl, text)

for key in highlights_to_add:
    content = add_highlight(key, content)

with open("own-bib.bib", "w") as f:
    f.write(content)

print("Updated highlights in own-bib.bib for Reddit role.")
