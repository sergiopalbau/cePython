from clases import GestioAlmacen, Producto

# Llama al método -listado- y muestra los productos existentes.

GestioAlmacen.listado()


# Usando el método “nuevo_producto”, añade dos productos nuevos. El segundo debe
# tener el mismo identificador que el primero. Comprueba si se añaden los dos o uno
# solo.

if GestioAlmacen.nuevo_producto(10, "pendientes", "accesorio", 5, 21, 10):
    print("añadido")

if GestioAlmacen.nuevo_producto(10, "pulsera", "accesorio", 3, 5, 3):
    print("añadido")

GestioAlmacen.listado()


# - Llama al método “bajo_mínimos” y guarda en una lista los productos que estén en
# mínimos. Muestra el contenido de la lista