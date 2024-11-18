"""
Para este ejercicio utilizaremos la lista de productos vista antes.
Accederemos al primer objeto de la lista y le añadiremos el atributo
 caducado con el valor True.
Recorremos la lista y visualizamos el atributo __dict__ de cada
objeto. Recuerdaque este atributo proporciona información sobre los
 atributos de un objeto, en forma de diccionario.

"""


class Producto ():

    def __init__(self, nombre: str, categoria: str, precio: float,
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
    productos = [Producto("tomate", "fruta", 2.3, 100),
                 Producto("patata", "verdura", 1.5, 200),
                 Producto("cebolla", "verdura", 1.8, 150),
                 Producto("manzana", "fruta", 3.2, 50),
                 Producto("pera", "fruta", 2.7, 75)]

    # añadir dinamicamente un atributo

    productos[0].caducado = True

    for p in productos:
        print(p.__dict__)
