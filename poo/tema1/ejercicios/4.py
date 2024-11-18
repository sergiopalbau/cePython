"""
Modificar la clase “Producto” del ejercicio anterior añadiendo un método que
actualice la cantidad de un producto sumándole un valor pasado como parámetro.
Mostrar los datos de un producto antes y después de ser modificada su cantidad


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

    def actualiza_stock(self, cantidad):
        self.cantidad += cantidad


if __name__ == "__main__":
    p1 = Producto("colonia", "perfume", 10, 20)
    print(p1.cantidad)
    p1.actualiza_stock(3)
    print(p1.cantidad)
