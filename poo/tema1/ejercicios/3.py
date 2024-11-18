"""Diseñar una clase Python llamada “Producto” con los atributos nombre,
 categoría,precio y cantidad. Diseña en esta clase el método __str__
 de forma que retorne todos los atributos en un dato de tipo cadena (str).
Crear dos productos pertenecientes a esa clase y mostrar todos los datos
de aquel producto que tenga mayor precio.
"""


class Producto ():

    def __init__(self, nombre: str, categoria: str, precio: int,
                 cantidad: int):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.cantidad = cantidad

    def __str__(self) -> str:
        return f"{self.nombre}-{self.categoria}-{self.precio}-{self.cantidad}"


if __name__ == "__main__":
    p1 = Producto("colonia", "perfume", 10, 20)
    p2 = Producto("colorete", "maquillaje", 5, 20)

    # Mostrar el producto de mayor precio

    if p1.precio > p2.precio:
        print(p1)
    else:
        print(p2)
