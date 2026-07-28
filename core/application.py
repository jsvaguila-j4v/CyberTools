from core.logger import Logger
from core.services import ServiceRegistry
from core.settings import Settings
class Application:
    def __init__(self): self.services=ServiceRegistry()
    def start(self): s=Settings(); l=Logger(); self.services.register("settings",s); self.services.register("logger",l); l.info("CyberTools Started"); print("CyberTools iniciado correctamente.")
