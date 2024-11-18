"""Visualizar en pantalla aquellos productos que pertenezcan a la 
categoría ‘verdura’.
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
    for p in productos:
        if p.categoria.lower() == "verdura":
            print(p)
