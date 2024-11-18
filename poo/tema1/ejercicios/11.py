"""Diseñar la clase “Empleado” con los atributos identificador, nombre,
 departamento,salario. Tener en cuenta que el salario será privado.
 Define un método para obtenerlo y otro para modificarlo.
Programa el método __eq__(), de forma que indique si dos empleados
son iguales o no en función de su salario.
Crear varios empleados, mostrar sus datos y comparar si son iguales o no.
"""


class Empleado():

    def __init__(self, identificador, nombre, departamento, salario):
        self.identificador = identificador
        self.nombre = nombre
        self.departamento = departamento
        self.__salario = salario  # atributo privado

    def get_salario(self):
        return (self.__salario)

    def modifica_salario(self, salario):
        self.__salario = salario

    def __eq__(self, empleado2):
        return self.__salario == empleado2.get_salario()


if __name__ == "__main__":
    e1 = Empleado(1, "Julio", "contabilidad", 1000)
    e2 = Empleado(2, "Cesar", "tecnico", 900)

    # obtener salario de emnplead1
    print(e1.get_salario())
    # Comparar los dos empleados en funcion del sueldo
    print(e1 == e2)

    # cambio de sueldo
    e2.modifica_salario(1000)
    print(e1 == e2)
