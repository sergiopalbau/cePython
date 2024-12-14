# clase base
class Persona:
    def __init__(self, nombre, apellidos, correo):
        self.nombre = nombre
        self.apellidos = apellidos
        self.correo = correo
    
    def __str__(self):
        return f"{self.nombre} {self.apellidos} {self.correo}"
    
# clase derivada

class Cliente(Persona):
    def __init__(self, nombre, apellidos, correo,num_cliente, numero_cuenta):
        super().__init__(nombre, apellidos, correo)
        self.num_cliente = num_cliente
        self.numero_cuenta = numero_cuenta
    
    def __str__(self):
        return super().__str__() + f" - {self.num_cliente} - {self.numero_cuenta}"
    
# clase derivada


class Trabajador(Persona):
    def __init__(self, nombre, apellidos, correo, num_trabajador, salario):
        super().__init__(nombre, apellidos, correo)
        self.num_trabajador = num_trabajador
        self.salario = salario
    
    def __str__(self):
        return super().__str__() + f" - {self.num_trabajador} - {self.salario}"
    

if __name__ == "__main__":
    cli1 = Cliente("Juan", "garcia", "ja@mail.com", 10, "ES123412")
    tra1 = Trabajador("ana", "Lopez", "ana@mail.com", 100, 1500)
    tra2 = Trabajador("pedro", "pica", "pica@mail.co", 200, 2000)

print(isinstance(tra1, Cliente))
print(issubclass(Persona, Cliente))

print(type(tra1).__name__)
print()