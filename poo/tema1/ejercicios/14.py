""" 14. Programar una agenda de contactos.
Definir la clase Contacto con los atributos nombre, teléfono y correo del contacto.

a. Añade el método __str__ para que retorne todos los atributos con el formato:
Nombre - teléfono - correo.
b. Programa también __repr__ para que retorne los datos del contacto con el
formato: Contacto(nombre, teléfono, correo).
c. Programa el método __eq__ para determinar si dos contactos son iguales.
En este caso serán iguales si coinciden todos los valores de sus atributos.
Programa la clase Agenda. Esta clase tendrá una lista de contactos y los métodos.
- Buscar contacto por nombre y retornar el contacto.
- Obtener el teléfono de un contacto. Retornar el teléfono.
- Obtener el correo de un contacto. Retornar el correo.
- Cambiar el teléfono de un contacto. Retornar True si se pudo hacer el
cambio, False en caso contrario.
- Cambiar el correo de un contacto. Retornar True si se pudo hacer el cambio,
False en caso contrario.
- Listar todos los contactos.
- Obtener el número de contactos"""


class Contacto:

    def __init__(self, nombre, telefono, correo):
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo
        pass

    """ a. Añade el método __str__ para que retorne todos los atributos con 
    el formato: 
    Nombre - teléfono - correo. """

    def __str__(self):
        return f"nombre: {self.nombre} -  telf: {self.telefono} - " \
         f"correo: {self.correo}"

    def __repr__(self):
        return f"Coctacto({self.nombre}, {self.telefono}, {self.correo})"

    def __eq__(self, otro):
        if self.nombre == otro.nombre and \
           self.telefono == otro.telefono and \
           self.correo == otro.correo:
            return True

        return False


class Agenda:

    lista_contactos = [Contacto("Juan", "11111", "jaun@mail.com"), 
                       Contacto("Mario", "22222", "mario@mail.com"),
                       Contacto("Maria", "33333", "maria@mail.com")]

    @classmethod
    def buscar_contacto(cls):
        pass

    @classmethod
    def obtener_telefono(cls, nombre):
        pass

    @classmethod
    def obtener_correo(cls, nombre):
        pass

    @classmethod
    def cambio_telefono(cls, nombre, telefono):
        pass

    @classmethod
    def cambio_correo(cls, nombre, correo):
        pass

    @classmethod
    def listar_contacto(cls):
        for contacto in cls.lista_contactos:
            print (contacto)

    @classmethod
    def contar_conctacos(cls):
        return len(cls.lista_contactos)

# ##################################################################################


if __name__ == "__main__":
    print("ejecutando programa")
    
