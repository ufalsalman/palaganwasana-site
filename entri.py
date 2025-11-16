import os
import json
from bs4 import BeautifulSoup

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ENTRI_DIR = os.path.join(BASE_DIR, "entri")
OUTPUT_JSON = os.path.join(ENTRI_DIR, "entri.json")

entries = []

for filename in os.listdir(ENTRI_DIR):
    if not filename.endswith(".html"):
        continue
    
    path = os.path.join(ENTRI_DIR, filename)
    mtime = os.path.getmtime(path)

    with open(path, "r", encoding="utf-8") as f:
        html = f.read()

    soup = BeautifulSoup(html, "html.parser")
    h1 = soup.find("h1")
    title = h1.get_text(strip=True) if h1 else filename

    entries.append({
        "file": filename,
        "title": title,
        "mtime": mtime
    })

entries.sort(key=lambda x: x["mtime"], reverse=True)

with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
    json.dump(entries, f, indent=2, ensure_ascii=False)

print("Generated:", OUTPUT_JSON)
