class ServiceRegistry:
    def __init__(self): self._s={}
    def register(self,n,v): self._s[n]=v
    def get(self,n): return self._s.get(n)
