import re

with open("own-bib.bib", "r") as f:
    content = f.read()

# Replace "Zhu, Rui" with "Zhu, R."
# Also handle cases with asterisk: "Zhu\textasteriskcentered, Rui" -> "Zhu\textasteriskcentered, R."
# Let's use a regex to capture anything between Zhu and Rui, like `\textasteriskcentered, `

# Specifically look for Zhu followed by optional formatting, then a comma and spaces, then Rui
# \textbf{Zhu, Rui} -> \textbf{Zhu, R.}
# \textbf{Zhu\textasteriskcentered, Rui} -> \textbf{Zhu\textasteriskcentered, R.}

content = re.sub(r'Zhu([^\,]*),\s*Rui', r'Zhu\1, R.', content)

with open("own-bib.bib", "w") as f:
    f.write(content)

print("Updated own-bib.bib to unify Zhu, Rui to Zhu, R.")
