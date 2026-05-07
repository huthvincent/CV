import re

with open("own-bib.bib", "r") as f:
    content = f.read()

# 1. xiong2025hey
# Old: Xiong, Chen and Wang, Zihao and \textbf{Zhu, Rui}
# New: Xiong\textasteriskcentered, Chen and Wang\textasteriskcentered, Zihao and \textbf{Zhu\textasteriskcentered, Rui}
content = content.replace(
    r"Xiong, Chen and Wang, Zihao and \textbf{Zhu, Rui}",
    r"Xiong\textasteriskcentered, Chen and Wang\textasteriskcentered, Zihao and \textbf{Zhu\textasteriskcentered, Rui}"
)

# 2. fan2025byzsfl
# Old: Fan\textasteriskcentered, Yongming\textasteriskcentered and \textbf{Zhu, Rui\textasteriskcentered}
# New: Fan\textasteriskcentered, Yongming and \textbf{Zhu\textasteriskcentered, Rui}
content = content.replace(
    r"Fan\textasteriskcentered, Yongming\textasteriskcentered and \textbf{Zhu, Rui\textasteriskcentered}",
    r"Fan\textasteriskcentered, Yongming and \textbf{Zhu\textasteriskcentered, Rui}"
)

# 3. chen2024janus
# Old: Chen\textasteriskcentered, Xiaoyi and Tang\textasteriskcentered, Siyuan\textasteriskcentered and \textbf{Zhu\textasteriskcentered, Rui}
# New: Chen\textasteriskcentered, Xiaoyi and Tang\textasteriskcentered, Siyuan and \textbf{Zhu\textasteriskcentered, Rui}
content = content.replace(
    r"Chen\textasteriskcentered, Xiaoyi and Tang\textasteriskcentered, Siyuan\textasteriskcentered and \textbf{Zhu\textasteriskcentered, Rui}",
    r"Chen\textasteriskcentered, Xiaoyi and Tang\textasteriskcentered, Siyuan and \textbf{Zhu\textasteriskcentered, Rui}"
)

# Function to add highlight to a specific entry
def add_highlight(key, text):
    # Regex to find keywords for a specific key
    pattern = r'(@[a-zA-Z]+\{'+key+r',[\s\S]*?keywords\s*=\s*\{)([^\}]+)(\})'
    def repl(m):
        kws = [k.strip() for k in m.group(2).split(',')]
        if 'highlight' not in kws:
            kws.insert(0, 'highlight')
        return m.group(1) + ', '.join(kws) + m.group(3)
    return re.sub(pattern, repl, text)

# 4 & 5. Add highlight to zhu2022SEAM, zhu2020privacy, and zhu2026foundation
content = add_highlight('zhu2022SEAM', content)
content = add_highlight('zhu2020privacy', content)
content = add_highlight('zhu2026foundation', content)

with open("own-bib.bib", "w") as f:
    f.write(content)

print("Updated own-bib.bib successfully.")
