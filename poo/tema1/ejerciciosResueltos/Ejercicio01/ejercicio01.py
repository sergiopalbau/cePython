# importación de la clase Vehiculo del módulo clases
from clases import Vehiculo

# creación de dos objetos de la clase Vehiculo	
v1 = Vehiculo("Toyota", "Corolla", 2015, 10000)
v2 = Vehiculo("Seat", "Ibiza", 2018, 8000)

# marca y modelo son de tipo texto
# precio es numérico, debe ser convertido a texto para poder concatenarlo
print(v1)
print(v2)

