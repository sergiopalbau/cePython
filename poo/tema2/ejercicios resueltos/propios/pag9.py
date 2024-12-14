from abc import ABC, abstractmethod

# clase abstracta


class Empleado(ABC):
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    # metodo abstracto
    @abstractmethod
    def get_info(self):
        pass


class Director(Empleado):
    def __init__(self, nombre, salario, bono):
        super().__init__(nombre, salario)
        self.bono = bono
    def get_info(self):
        return "hola"


if __name__ == "__main__":
    d= Director("juan", 1000, 210)
    e = Empleado("no",122)