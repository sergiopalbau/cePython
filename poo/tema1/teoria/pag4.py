class Empleado:
    contador = 0   #atributo de clase, se mantiene en cada objeto de forma común
    def __init__(self, nombre, salario):
        self.nombre= nombre
        self.salario= salario
        Empleado.contador +=1 #incrementa el contador de empleados

    def aumento_salario(self, porcentaje):
        self.salario = self.salario + self.salario * porcentaje

#############################################################################################
emp1 = Empleado ("juan",2000)
emp2 = Empleado ("David",3000)

print (emp1.contador)
print (emp2.contador)
print (Empleado.contador)

