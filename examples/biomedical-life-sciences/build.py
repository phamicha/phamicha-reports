from pathlib import Path
import json
p=Path(__file__).parent
d=json.loads((p/"data.json").read_text())
s=(p/"template.html").read_text().replace("__DATA__",json.dumps(d,ensure_ascii=False).replace("<", "\\u003c"))
(p/"index.html").write_text(s)
print("Created index.html")
