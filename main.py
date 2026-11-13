import os

d = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
os.makedirs(d, exist_ok=True)
open(d + "/entry.txt", "w").write("My tests failed, so my agent fixed them — it deleted the assertions.")
