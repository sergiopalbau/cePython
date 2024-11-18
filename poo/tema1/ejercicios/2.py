"""En este ejercicio utilizaremos la misma clase que en el ejercicio anterior y
añadiremos un método llamado “nombre_completo” que retorne en una cadena los
atributos marca y modelo concatenados y separados por un guión (Seat-Ibiza).
Crear dos objetos y probar el método.
"""


class Vehiculo ():

    def __init__(self, marca: str, modelo: str, año: int, precio: float):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.precio = precio

    def nombre_completo(self):
        return f"{self.marca}-{self.modelo}"

    def __str__(self):
        return (f"{self.marca} {self.modelo} {self.precio}")


if __name__ == "__main__":

    coche1 = Vehiculo("ford", "Sierra", 1996, 3500.0)
    coche2 = Vehiculo("Opel", "Kadet", 1996, 3000.0)

    print(coche1)
    print(coche2)

    print(coche1.nombre_completo())
    print(coche2.nombre_completo())
