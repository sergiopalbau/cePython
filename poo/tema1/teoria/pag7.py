class Persona():
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.__edad = edad #atributo privado

    def edad_persona (self):
        return self.__edad


per1 = Persona("Juan",30)
per2 = Persona ("Luis",25)

print (per1.nombre)
print (per1.edad_persona()) #acceso por  el metodo
print (per1._Persona__edad)  #atributo privado acceso directo

try:
    print (per1.__edad)
except (AttributeError):
    print ("Genero error pq no puedo leer")


