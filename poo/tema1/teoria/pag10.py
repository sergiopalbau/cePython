class Empleado ():
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario
    
    def __str__(self):
        return f"Nombre: {self.nombre}, salario {self.salario}"
    
    def __eq__ (self, otro):
        return self.salario == otro.salario
    
    def __repr__(self):
        return f"Nombre: {self.__dict__}"
    
    def __len__ (self):
        return len(self.nombre)
    

#####################################################

emp1 = Empleado("Juan",1500)
emp2 = Empleado("paco",2000)

#llamada __str__
print(emp1)

#llamada __eq__
print (emp1 == emp2)

#llamada a __repr__
print (repr(emp1))

