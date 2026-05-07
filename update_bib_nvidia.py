import re

highlights_to_add = [
    "zhu2026foundation",
    "zhu2023DPAdapter",
    "wang2025sharpness",
    "chen2024janus",
    "xiong2025hey"
]

with open("own-bib.bib", "r") as f:
    content = f.read()

def replace_keywords(match):
    key = match.group(1)
    keywords_str = match.group(2)
    # Split keywords, strip whitespace
    keywords = [k.strip() for k in keywords_str.split(',')]
    
    # Remove 'highlight' if it's there
    if 'highlight' in keywords:
        keywords.remove('highlight')
        
    # Add 'highlight' if it's in our list
    if key in highlights_to_add:
        keywords.insert(0, 'highlight')
        
    return f"@{match.group(3)}{{{key},\n{match.group(4)}keywords      = {{{', '.join(keywords)}}}"

# Regex to find citation key and keywords field
# This is a bit tricky with regex, let's use a simpler approach
# We can iterate over the lines, or use a specific regex.
# @article{zhu2026foundation, ... keywords = {published, highlight} }

pattern = r'@([a-zA-Z]+)\{([^,]+),([\s\S]*?)keywords\s*=\s*\{([^\}]+)\}'

def repl(m):
    entry_type = m.group(1)
    key = m.group(2)
    middle = m.group(3)
    kws = m.group(4).split(',')
    kws = [k.strip() for k in kws if k.strip() != 'highlight']
    if key in highlights_to_add:
        kws.insert(0, 'highlight')
    return f"@{entry_type}{{{key},{middle}keywords      = {{{', '.join(kws)}}}"

new_content = re.sub(pattern, repl, content)

with open("own-bib.bib", "w") as f:
    f.write(new_content)

print("Updated own-bib.bib for NVIDIA")
