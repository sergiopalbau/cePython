"""
9. Calcular la media de todos los precios de los productos.
"""

from clases import Producto

cuenta = 0

# Lista de productos
productos = [Producto("tomate", "fruta", 2.3, 100),
             Producto("patata", "verdura", 1.5, 200),
             Producto("cebolla", "verdura", 1.8, 150),
             Producto("manzana", "fruta", 3.2, 50),
             Producto("pera", "fruta", 2.7, 75)]
cuenta_productos = 0
suma_precios = 0
for p in productos:
    suma_precios += p.precio
    cuenta_productos += 1
print(suma_precios/cuenta_productos, "media de los precios")
