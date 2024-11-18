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
        return f"{self.identificador} {self.nombre} {self.categoria}"\
              f" {self.precio} {self.stock}"\
              f" {self.stock_minimo}"

    def __eq__(self, otro):
        return self.identificador == otro.identificador


#      ######################################################### #

class GestioAlmacen ():
    # atributos de clase
    productos = [Producto(1, "calcetines", "interior", 1, 33, 10),
                 Producto(2, "camiseta", "superior", 4, 25, 5),
                 Producto(3, "corbata", "accesorio", 2, 3, 5)
                 ]

    @classmethod
    def nuevo_producto(cls, id, nombre, categoria, precio, stock, stock_min):
        """Recibe datos de un producto como argumentos y lo añade a la lista,
        siempre y cuando su identificador no exista en la misma. Retorna
        True si el producto se añadió a la lista, False en caso contrario."""

        nuevo_producto = Producto(id, nombre, categoria, precio, stock,
                                  stock_min)
        if cls.buscar_por_id(nuevo_producto.identificador):
            # el producto existe
            print("El id ya esta en la lista, no se añade")
            return False
        else:
            cls.productos.append(nuevo_producto)
            return True

    @classmethod
    def buscar_por_id(cls, id):
        """buscar_por_id. Recibe un identificador de producto como argumento y
        lo busca en la lista. En caso de encontrarlo lo retorna, si no lo
        encuentra debe retornar el valor None"""
        for producto in cls.productos:
            if producto.identificador == id:
                return producto
        return None

    @classmethod
    def bajo_minimos(cls):
        """bajo_minimos. Retorna una lista con los productos que estén
         bajo mínimos."""
        bajo_minimo = []
        for producto in cls.productos:
            if producto.esta_en_minimos():
                bajo_minimo.append(producto)
        return bajo_minimo

    @classmethod
    def listado(cls):
        """listado. Muestra en pantalla un listado de los productos existentes
          en el almacén"""
        print()  # salto de linea
        for producto in cls.productos:
            print(producto)
        print()  # salto de linea



