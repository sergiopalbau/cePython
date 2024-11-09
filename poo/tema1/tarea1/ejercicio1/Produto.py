class Producto ():
    def __init__(self, identificador, nombre, categoria, precio, stock, stock_minimo):
        self.identificador = identificador
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.stock = stock
        self.stock_minimo = stock_minimo
    
    def actualizar_stock (self, cantidad):
        self.stock += cantidad

    def esta_en_minimos (self):
        return self.stock < self.stock_minimo

    def __str__ (self):
        return f"{self.nombre} = {self.stock} unidades"
    
    def __eq__ (self, otro):
        return self.identificador == otro.identificador