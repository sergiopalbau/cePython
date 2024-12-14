class Triangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura / 2


class Circulo:

    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return 3.14159 * self.radio ** 2
    
if __name__ == "__main__":
    
    def calcular(figura):
        return figura.area()
    c = Circulo(3)
    t = Triangulo(4,3)

    print(calcular(c))
    print(calcular(t))
