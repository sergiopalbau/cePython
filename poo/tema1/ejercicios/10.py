""" 
Diseñar una clase llamada “Mates” con los métodos estáticos que se describen:
a. mayor. Recibe dos números como argumento y retorna el mayor.
b. producto. Recibe tres números como argumento y retorna su producto.
c. potencia. Recibe una base y un exponente como argumentos y retorna la
base elevada al exponente.
Probar los métodos programados.
"""


class Mates ():
    @staticmethod
    def mayor(n1, n2):
        if n1 > n2:
            return n1
        return n2

    @staticmethod
    def producto(n1, n2, n3):
        return n1 * n2 * n3

    @staticmethod
    def potencia(n1, n2):
        return n1**n2


if __name__ == "__main__":
    print(Mates.mayor(10, 30))
    print(Mates.producto(2, 5, 10))
    print(Mates.potencia(2, 3))
