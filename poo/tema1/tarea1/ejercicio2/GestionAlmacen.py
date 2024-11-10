from Produto import Producto


class GestioAlmacen ():
    # atributos de clase
    productos = []

    def __init__(self):
        # comprobamos si el atributo de clase ha sido inicializado si 
        # la primera vez no tendria pq tener productos.
        if len(self.productos) == 0:
            prod1 = Producto(1, "calcetines", "interior", 1, 33, 10)
            prod2 = Producto(2, "camiseta", "superior", 4, 25, 5)
            prod3 = Producto(3, "corbata", "accesorio", 2, 3, 5)
            GestioAlmacen.productos.append(prod1)
            GestioAlmacen.productos.append(prod2)
            GestioAlmacen.productos.append(prod3)

    def nuevo_producto(self, id, nombre, categoria, precio, stock, stock_min):
        """Recibe datos de un producto como argumentos y lo añade a la lista,
        siempre y cuando su identificador no exista en la misma. Retorna
        True si el producto se añadió a la lista, False en caso contrario."""

        nuevo_producto = Producto(id, nombre, categoria, precio, stock, 
                                  stock_min)      
        # TODO comrpobar si el producto esta en el listado
        GestioAlmacen.buscar_por_id(nuevo_producto.identificador)

    def buscar_por_id(self, id):
        """buscar_por_id. Recibe un identificador de producto como argumento y
        lo busca en la lista. En caso de encontrarlo lo retorna, si no lo
        encuentra debe retornar el valor None"""

        for producto in GestioAlmacen.productos:
            if producto.identificador == id:
                print("el producto existe!!")
                return producto
            return None

    def bajo_minimos(self):
        """bajo_minimos. Retorna una lista con los productos que estén
         bajo mínimos."""
        bajo_minimo = []
        for producto in GestioAlmacen.productos:
            if producto.esta_en_minimos():
                bajo_minimo.append(producto)
                print(f"{producto} en minimos")

        return bajo_minimo

    def listado(self):
        """listado. Muestra en pantalla un listado de los productos existentes
          en el almacén"""
        print()  # salto de linea
        for producto in GestioAlmacen.productos:
            print(producto)
        print()  # salto de linea


if __name__ == "__main__":

    # listar los productos
    almacen = GestioAlmacen()
    almacen.listado()
    almacen.bajo_minimos()

    # almacen.buscar_por_id(1)

    almacen.nuevo_producto(1, "capa", "accesorio")
