import re

with open("own-bib.bib", "r") as f:
    content = f.read()

# Pattern to find entries
entry_pattern = re.compile(r'(@[a-zA-Z]+\{([^,]+),([\s\S]*?)(?=\n@|\Z))', re.IGNORECASE)

highlights_to_add = []
for full_match, key, body in entry_pattern.findall(content):
    if re.search(r'(USENIX Security|NDSS|Computer and Communications Security|S\\&P)', body, re.IGNORECASE):
        highlights_to_add.append(key)

print(f"Found keys to highlight: {highlights_to_add}")

# First, remove 'highlight' from everywhere
def remove_highlight(match):
    kws = match.group(1).split(',')
    kws = [k.strip() for k in kws if k.strip() != 'highlight']
    if not kws:
        kws = ['others'] # fallback if empty
    return f"keywords      = {{{', '.join(kws)}}}"

content = re.sub(r'keywords\s*=\s*\{([^\}]+)\}', remove_highlight, content)

# Now, add 'highlight' to the designated entries
def add_highlight(key, text):
    pattern = r'(@[a-zA-Z]+\{'+re.escape(key)+r',[\s\S]*?keywords\s*=\s*\{)([^\}]+)(\})'
    def repl(m):
        kws = [k.strip() for k in m.group(2).split(',')]
        if 'highlight' not in kws:
            kws.insert(0, 'highlight')
        return m.group(1) + ', '.join(kws) + m.group(3)
    
    new_text = re.sub(pattern, repl, text)
    if new_text == text:
        print(f"Warning: Failed to add highlight to {key}")
    return new_text

for key in highlights_to_add:
    content = add_highlight(key, content)

with open("own-bib.bib", "w") as f:
    f.write(content)

print("Updated own-bib.bib with new highlights for DeepMind role.")
