from clases import GestioAlmacen

# Llama al método -listado- y muestra los productos existentes.
print("\nListado de productos en almacén ------------------")
GestioAlmacen.listado()


# Usando el método “nuevo_producto”, añade dos productos nuevos. El segundo
#  debe  tener el mismo identificador que el primero. Comprueba si se
#  añaden los dos o uno # solo.
print("intentando añadir productos -----------------------")
if GestioAlmacen.nuevo_producto(10, "pendientes", "accesorio", 5, 21, 10):
    print("añadido")
else:
    print("no se puede añadir")

if GestioAlmacen.nuevo_producto(10, "pulsera", "accesorio", 3, 5, 3):
    print("añadido")
else:
    print("no se puede añadir")

GestioAlmacen.listado()

# - Llama al método “bajo_mínimos” y guarda en una lista los productos
# que estén en # mínimos. Muestra el contenido de la lista
print("Imprimiendo listado de productos en minimos .------")
listado_minimo = GestioAlmacen.bajo_minimos()
for producto in listado_minimo:
    print(producto)
