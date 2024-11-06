class Partido:
    def __init__ (self, local:str, visitante:str, puntosLocal:int, puntosVisitante:int):
        """__init__  - constructor de la clase

        Args:
            local (str): equipo local
            visitante (str): equipo visitante
            puntosLocal (int): puntos del equipo Local
            puntosVisitante (int): puntos del equipo visitante
        """
        self.local = local
        self.visitante = visitante
        self.puntosLocal = puntosLocal
        self.puntosVisitante=puntosVisitante