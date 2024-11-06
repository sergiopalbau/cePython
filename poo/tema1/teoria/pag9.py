class Empleado():

    def __init__ (self, nombre, salario):
        self.nombre = nombre
        self.salario = salario
emp = Empleado ("Juan",1000)
# acceder al nombre
print (getattr(emp,"nombre"))

#modificar el salario
setattr (emp,"salario",2000)
print (getattr(emp,"salario"))

#comprobar si el atributo existe
print (hasattr(emp,"edad"))
print (hasattr(emp,"salario"))
delattr(emp,"salario")
print(hasattr(emp,"salario"))
print (dir(emp))
print (emp.__dict__)

