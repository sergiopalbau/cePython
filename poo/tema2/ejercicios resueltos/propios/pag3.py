class Equipo:
    def __init__(self,nombre, ciudad):
        self.nombre = nombre
        self.ciudad = ciudad
    
    def __str__(self):
        return f"{self.nombre} de {self.ciudad}"
    
    def __eq__(self, otro):
        return self.nombre == otro.nombre and self.ciudad == otro.ciudad
    
# clase contenedora

class Campeonato:

    def __init__(self, nombre, año, descripcion):
        self.nombre = nombre
        self.año = año
        self.descripcion = descripcion
        self.equipos  = []
    
    def __str__(self):
        return f"{self.nombre} de {self.ciudad} - {self.equipo}"
    
    def agregar_equipo(self, equipo):
        # comprobar si el equipo esta en la lista
        #funciona pq ya existe __eq_ en la clase equipo

        if equipo in self.equipos:
            return False
        self.equipos.append(equipo)
        return True
    
if __name__ == "__main__":
    liga = Campeonato("liga", 2021, "Campeonato Futbol")

    madrid = Equipo ("Madrid","Madrid")
    betis = Equipo ("betis", "sevilla")

    liga.agregar_equipo(madrid)
    liga.agregar_equipo(betis)
    liga.agregar_equipo(Equipo("athletic", "bilbao"))

    for equipo in liga.equipos:
        print(equipo)