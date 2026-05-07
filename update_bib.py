import re

# Define the categorizations
categories = {
    "zhu2026foundation": "highlight, ai4s",
    "zhu2026large": "ai4s",
    "zhu2025CoReason": "others",
    "zhu2025BHI": "trustworthy",
    "ge2025BMI": "ai4s",
    "zhu2024ADetectoLocum": "ai4s",
    "ge2025SSB": "ai4s",
    "zhang2025KedrecLM": "ai4s",
    "zhu2023ARO": "trustworthy",
    "wang2025sharpness": "trustworthy",
    "fan2025byzsfl": "trustworthy",
    "ma2025enhancing": "ai4s",
    "zhu2025near": "highlight, ai4s",
    "zhu2025advancing": "highlight, ai4s",
    "xiong2025hey": "trustworthy",
    "li2025adversarial": "trustworthy",
    "li2025knowledge": "others",
    "li2025memorization": "trustworthy",
    "zhu2022GRASP": "trustworthy",
    "zhu2023DPAdapter": "trustworthy",
    "chen2024janus": "trustworthy",
    "zhu2022TSA": "trustworthy",
    "zhu2023SEAMfair": "trustworthy",
    "zhu2022SEAM": "trustworthy",
    "zhu2022sigir": "others",
    "zhu2022bigdata": "others",
    "zhu2020privacy": "trustworthy",
    "zhu2020bounding": "others"
}

with open("own-bib.bib", "r") as f:
    content = f.read()

# For each entry, we find the citation key and replace its keywords
for key, keywords in categories.items():
    # Regex to match the entry block and replace keywords
    # This looks for @<type>{<key>, ... keywords = {<old_keywords>} ... }
    # Since bibtex-tidy aligned things, there might be spaces.
    pattern = r'(@[a-zA-Z]+\{'+key+r',[\s\S]*?keywords\s*=\s*\{)[^\}]*(\})'
    content = re.sub(pattern, r'\g<1>' + keywords + r'\g<2>', content)

with open("own-bib.bib", "w") as f:
    f.write(content)

print("Updated own-bib.bib")
