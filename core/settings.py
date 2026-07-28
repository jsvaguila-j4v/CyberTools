import json
from pathlib import Path
class Settings:
    def __init__(self): self.data=json.loads(Path("config/settings.json").read_text(encoding="utf-8"))
    def get(self,k,d=None): return self.data.get(k,d)
