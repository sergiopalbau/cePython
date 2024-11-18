# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 18:03:32 2024

@author: sergio
"""

"""
Diseñar una clase llamada “Vehículo” con los atributos marca, modelo, año y
 precio.

Crear dos objetos pertenecientes a esa clase e imprimir en pantalla la marca,
el modelo y el precio de cada vehículo (mediante __str__).
"""


class Vehiculo ():

    def __init__(self, marca: str, modelo: str, año: int, precio: float):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.precio = precio

    def __str__(self):
        return (f"{self.marca} {self.modelo} {self.precio}")


if __name__ == "__main__":

    coche1 = Vehiculo("ford", "Sierra", 1996, 3500.0)
    coche2 = Vehiculo("Opel", "Kadet", 1996, 3000.0)

    print(coche1)
    print(coche2)
