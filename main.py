import os
from pathlib import Path

JOKE = "I asked my agent to estimate the ticket. It estimated how long it would take me to explain it."
out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out.mkdir(parents=True, exist_ok=True)
(out / "entry.txt").write_text(JOKE, encoding="utf-8")
