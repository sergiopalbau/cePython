"""
btener la media de los precios de los productos de la categoría ‘verdura’.
"""

from clases import Producto

# lista inicial del productos

productos = [Producto("tomate", "fruta", 2.3, 100),
             Producto("patata", "verdura", 1.5, 200),
             Producto("cebolla", "verdura", 1.8, 150),
             Producto("manzana", "fruta", 3.2, 50),
             Producto("pera", "fruta", 2.7, 75)]

cantidad_verduras = 0
pvp_productos = 0


for producto in productos:
    if producto.categoria.lower() == "verdura":
        cantidad_verduras += 1
        pvp_productos += producto.precio
# calulo de la media
media = pvp_productos / cantidad_verduras

print(str(media))
