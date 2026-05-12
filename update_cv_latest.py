import re

highlights_to_add = [
    "zhu2025advancing",
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

# Fix author formatting for Zhu, R.
# Replace all bad \textbf{...Zhu...} with correct BibTeX format
# E.g., \textbf{Zhu\textasteriskcentered, R.} -> {\textbf{Zhu}}\textasteriskcentered, {\textbf{R.}}
# \textbf{Zhu, R.} -> {\textbf{Zhu}}, {\textbf{R.}}

# We'll just manually fix zhu2024ADetectoLocum as requested, and a global replace for the others
# Currently zhu2024ADetectoLocum:
# author        = {Mortensen\textasteriskcentered, Genevieve\textasteriskcentered and \textbf{Zhu\textasteriskcentered, R.}},
# Fix to:
# author        = {Mortensen\textasteriskcentered, Genevieve and {\textbf{Zhu}}\textasteriskcentered, {\textbf{R.}}},

content = content.replace(
    r"Mortensen\textasteriskcentered, Genevieve\textasteriskcentered and \textbf{Zhu\textasteriskcentered, R.}",
    r"Mortensen\textasteriskcentered, Genevieve and {\textbf{Zhu}}\textasteriskcentered, {\textbf{R.}}"
)

# And let's fix all other occurrences of \textbf{Zhu\textasteriskcentered, R.} just in case
content = content.replace(
    r"\textbf{Zhu\textasteriskcentered, R.}",
    r"{\textbf{Zhu}}\textasteriskcentered, {\textbf{R.}}"
)

content = content.replace(
    r"\textbf{Zhu, R.}",
    r"{\textbf{Zhu}}, {\textbf{R.}}"
)

# Also fix the ones that might have \textbf{Zhu}, \textbf{R.} to {\textbf{Zhu}}, {\textbf{R.}}
# Actually the above replace does \textbf{Zhu, R.} -> {\textbf{Zhu}}, {\textbf{R.}}

with open("own-bib.bib", "w") as f:
    f.write(content)

print("Updated own-bib.bib with new highlights and author formatting.")
