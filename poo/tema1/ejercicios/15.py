class Ciudad:

    def __init__(self, nombre, poblacion, pais, continente):
        self.nombre = nombre
        self.poblacion = poblacion
        self.pais = pais
        self.continente = continente

    def __eq__(self, otra):
        if self.nombre == otra.nombre \
         and self.pais == otra.pais:
            return True
        return False

    def __str__(self):
        return f"{self.nombre} - {self.poblacion} - {self.pais}"\
              + f" - {self.continente}"


# Gestion_ciudades #########################################################

class Gestion_ciudades:

    # atributo de clase

    lista_cities = [
                    Ciudad("Bogotá", 8000000, "Colombia", "América"),
                    Ciudad("Lima", 10000000, "Peru", "América"),
                    Ciudad("Paris", 5000000, "Francia", "Europa"),
                    Ciudad("Berlin", 4000000, "Alemania", "Europa"),
                    Ciudad("Tokio", 9000000, "Japón", "Asia"),
                    Ciudad("Sydney", 3000000, "Australia", "Oceanía"),
                    Ciudad("Johannesburgo", 5000000, "Sudáfrica", "África"),
                    Ciudad("Moscú", 10000000, "Rusia", "Europa"),
                    Ciudad("Nueva York", 8000000, "Estados Unidos", "América"),
                    Ciudad("Sao Paulo", 12000000, "Brasil", "América"),
                    Ciudad("Buenos Aires", 15000000, "Argentina", "América"),
                    Ciudad("Londres", 9000000, "Reino Unido", "Europa"),
                    Ciudad("Roma", 4000000, "Italia", "Europa"),
                    Ciudad("Pekín", 20000000, "China", "Asia"),
                    Ciudad("Delhi", 15000000, "India", "Asia"),
                    Ciudad("El Cairo", 7000000, "Egipto", "África"),
                    Ciudad("Ciudad del Cabo", 4000000, "Sudáfrica", "África"),
                    Ciudad("Melbourne", 5000000, "Australia", "Oceanía"),
                    Ciudad("Auckland", 2000000, "Nueva Zelanda", "Oceanía"),
                    Ciudad("Brisbane", 3000000, "Australia", "Oceanía"),
                    Ciudad("Madrid", 6000000, "España", "Europa"),
                    Ciudad("Lisboa", 3000000, "Portugal", "Europa"),
                    ]

    @classmethod
    def mostrar_ciudad_continente(cls, continente):
        """ Mostrar las ciudades de un continente dado."""
        lista = cls.lista_continente(continente)
        for ls in lista:
            print(ls.nombre)

    @classmethod
    def mostrar_ciudad_poblacion(cls, numero):
        """ Mostrar las ciudades con una población mayor que un número dado."""

        for p in cls.lista_cities:
            if p.poblacion > numero:
                print(p)

        print()
        pass

    @classmethod
    def ciudades_pais(cls, pais):
        """ Retornar el número de ciudades de un país dado"""
        numero_ciudades = 0
        for c in cls.lista_cities:
            if c.pais.lower() == pais.lower():
                numero_ciudades += 1
        return numero_ciudades

    @classmethod
    def ciudades_cadena(cls, cadena):
        """ Retornar el número de ciudades que contienen una cadena en su nombre"""
        for ciudad in cls.lista_cities:
            
        pass

    @classmethod
    def poblacion_pais(cls, pais):
        """ Retornar la media de la población de las ciudades de un país """
        lista = cls.lista_pais(pais)
        numero_ciudades = 0
        cuenta_poblacion = 0
        for ls in lista:
            numero_ciudades += 1
            cuenta_poblacion += ls.poblacion
        return cuenta_poblacion/numero_ciudades

    @classmethod
    def lista_pais(cls, pais):
        """ Retornar una lista con las ciudades de un país."""
        lista = []
        for p in cls.lista_cities:
            if pais.lower() == p.pais.lower():
                lista.append(p)
        return lista

    @classmethod
    def lista_continente(cls, continente):
        """ Retornar una lista con las ciudades de un continente."""
        lista = []
        for c in cls.lista_cities:
            if continente.lower() == c.continente.lower():
                lista.append(c)
        return lista

    @classmethod
    def habitantes_global(cls):
        """ Retornar la suma de los habitantes de todas las ciudades"""

        suma_poblacion = 0
        for c in cls.lista_cities:
            suma_poblacion += c.poblacion

        return suma_poblacion

    @classmethod
    def añadir_ciudad(cls, ciudad):
        """ Añadir ciudad. Este método recibe un objeto ciudad como parámetro e
        intenta añadir esa ciudad a la lista. Si la ciudad está en la lista no
        podrá añadirla y retornará False. En caso de añadirla el retorno será 
        True. Para comprobar si un valor está en una lista se puede utilizar:
        - if valor in lista
        - if valor not in lista"""
        if ciudad in cls.lista_cities:
            return False
        cls.lista_cities.append(ciudad)
        return True


###############################################################################
if __name__ == "__main__":
    print()
    print(Gestion_ciudades.habitantes_global())
    # print(Gestion_ciudades.mostrar_ciudad_poblacion(100_300_000))

    lista2 = Gestion_ciudades.lista_continente("américa")
    
    for p in lista2:
        print(p)
    
    print()

    lista3 = Gestion_ciudades.lista_pais("brasil")
    
    for p in lista3:
        print(p)
        
    Gestion_ciudades.mostrar_ciudad_continente("américa")

    print(Gestion_ciudades.ciudades_pais("españa"))

    print(Gestion_ciudades.poblacion_pais("españa"))

    print(Gestion_ciudades.añadir_ciudad(Ciudad("leon", 160000, "España", "Europa")))

    print (Gestion_ciudades.ciudades_pais("españa"))


