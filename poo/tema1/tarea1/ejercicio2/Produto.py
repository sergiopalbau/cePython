class Producto ():
    def __init__(self, identificador, nombre, categoria, precio, stock,
                 stock_minimo):
        """producto --

        Args:
            identificador (int): referencia del producto
            nombre (str): nombre del producto
            categoria (str): categoria en la que se clasifica en el almacen
            precio (int): precio de venta
            stock (int): elementos en el almacen
            stock_minimo (int): cantidad de elementos minimos que deben haber
            en el almacen
        """
        self.identificador = identificador
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.stock = stock
        self.stock_minimo = stock_minimo

    def actualizar_stock(self, cantidad):
        self.stock += cantidad

    def esta_en_minimos(self):
        return self.stock < self.stock_minimo

    def __str__(self):
        return f"{self.nombre} {self.categoria} {self.precio} {self.stock}"\
              f" {self.stock_minimo}"

    def __eq__(self, otro):
        return self.identificador == otro.identificador
