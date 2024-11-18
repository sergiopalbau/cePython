""" Diseñar una aplicación Python que trabaje con objetos de la clase “Partido”.
 Cada artido tendrá como atributos equipo local, equipo visitante, goles local, 
 goles visitante, campeonato y fecha.

La aplicación consta también de una clase llamada “GestionPartidos” que tendrá
como atributo de clase una lista de partidos y los métodos siguientes:
- Filtrar por equipo local. Recibe un equipo local como argumento e imprime
todos los partidos de ese equipo actuando como local.
- Ganados del equipo. Recibe un equipo como argumento y retorna cuántos
partidos ganó ese equipo, independientemente de si actuó como local o
como visitante.
- Mostrar los partidos del año pasado como parámetro.
- Mostrar los partidos de una fecha pasada como parámetro.
- Añadir un nuevo partido a la lista de partidos.
- Cuenta partidos. Retorna el número de partidos de la lista.
Prueba las clases y los métodos creados.

"""

from datetime import datetime


class Partido:
    def __init__(self, local, visitante,
                 goles_local,
                 goles_visitante,
                 campeonato,
                 fecha):
        self.local = local
        self.visitante = visitante
        self.goles_local = goles_local
        self.goles_visitantes = goles_visitante
        self.campeonato = campeonato
        self.fecha = fecha

    def __str__(self):
        return f"{self.local} vs {self.visitante} -> {self.goles_local} {self.goles_visitantes} - {self.campeonato} - {self.fecha}"
                 


class GestionPartidos:

    partidos = [Partido("Real Madrid", "Barcelona", 2, 1, "Liga", datetime(2021, 10, 20)),
                Partido("Betis", "Sevilla", 1, 1, "Liga", datetime(2021, 10, 21)),
                Partido("Real Madrid", "Sevilla", 3, 0, "Liga", datetime(2021,10,26)),
                Partido("Betis", "Barcelona", 0, 0, "Liga", datetime(2021,10,27)),
                Partido("Real Madrid", "Betis", 2, 2, "Liga", datetime(2021,10,28)),
                Partido("Sevilla", "Barcelona", 1, 0, "Liga", datetime(2022,10,29)),
                Partido("Sevilla", "Real Madrid", 1, 3, "Liga", datetime(2022,10,29))
                ]

    @classmethod
    def filtrar_por_local(cls, local):
        """ Recibe un equipo local como argumento e imprime
        to_dos los partidos de ese equipo actuando como local"""
        for p in cls.partidos:
            if p.local.lower() == local.lower():
                print(p)

    @classmethod
    def ganados_equipo(cls, equipo):
        """ Ganados del equipo. Recibe un equipo como argumento y retorna
        cuántos partidos ganó ese equipo, independientemente de
        si actuó como local o como visitante. """
        partidos_ganados =[]
        for p in cls.partidos:
            # comprobamos si el equipo participo como local y gano
            if p.local.lower() == equipo.lower() and p.goles_local > p.goles_visitantes:
                print(p)
                partidos_ganados.append(p)
            # comprobamos si el equipo participo como visitante y gano
            if p.visitante.lower() == equipo.lower() and p.goles_local < p.goles_visitantes:
                print(p)
                partidos_ganados.append(p)

        return partidos_ganados

    @classmethod
    def mostrar_partidos_año(cls, año):
        """ Mostrar los partidos del año pasado como parámetro."""
        for p in cls.partidos:
            if p.fecha.year == año:
                print(p)

    @classmethod
    def partidos_fecha(cls, fecha):
        """ Mostrar los partidos de una fecha pasada como parámetro."""
        for p in cls.partidos:
            if p.fecha == fecha:
                print(p)

    def añadir_partido(self, partido):
        """ Añadir un nuevo partido a la lista de partidos."""
        pass

    @classmethod    
    def cuenta_partidos(cls):
        """ Retorna el número de partidos de la lista."""
        return len(cls.partidos)


if __name__ == "__main__":

    # GestionPartidos.filtrar_por_local("betis")
    print()
    # GestionPartidos.ganados_equipo("Real madrid")
    print()
    # GestionPartidos.mostrar_partidos_año(2021)
    fecha2 = datetime(2022, 10, 29)
    GestionPartidos.partidos_fecha(fecha2)
