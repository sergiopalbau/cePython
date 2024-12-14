#delegacion

class Motor:

    def __init__(self, cilindros, tipo):
        self.cilindros = cilindros
        self.tipo = tipo

    def __str__(self):
        return f"Motor de {self.cilindros} cilindros {self.tipo}"
    
    def __eq__(self, value):
        return self.cilindros == value.cilindros and self.tipo == value.tipo
    
# clase contenedora

class Vehiculo:

    def __init__(self, marca, modelo, cilindros, tipo):
        self.marca = marca
        self.model = modelo 
        self.motor = Motor(cilindros, tipo)  # delegacion
    
    def __str__(self):
        return f"{self.marca} {self.model} {self.motor}"
    
    def compara_motor(self,otro):
        return self.motor == otro.motor
    

if __name__ == "__main__":

    fiesta = Vehiculo("ford", "fiesta", 4, "gasolina")
    print(fiesta)

    rio = Vehiculo("Kia", "rio", 4, "gasolina")
    print(rio)

    print(fiesta.compara_motor(rio))

