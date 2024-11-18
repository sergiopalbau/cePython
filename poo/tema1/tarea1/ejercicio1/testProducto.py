from Produto import Producto

# instanciar los objetos
producto1 = Producto(1, "calcetin","ropa", 3, 100, 20)
producto2 = Producto(2, "camiseta","ropa", 3, 25, 10)

# imprimir los productos
print(producto1)
print(producto2)

# actualizar unidades del primero
n = 5
print("añadir en ", n, "unidades el producto 2")
producto1.actualizar_stock(n)
print(producto1)

# comprobar stock minimo
print("esta en minimo el producto 2", producto2.stock_minimo)

# comprobar si son iguiales

print("son iguales", producto1 == producto2)
