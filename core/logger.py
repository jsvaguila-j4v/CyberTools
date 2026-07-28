import logging
from pathlib import Path
Path("logs").mkdir(exist_ok=True)
logging.basicConfig(filename="logs/cybertools.log",level=logging.INFO,format="%(asctime)s | %(levelname)s | %(message)s")
class Logger:
    def __init__(self): self.logger=logging.getLogger("CyberTools")
    def info(self,m): self.logger.info(m)
