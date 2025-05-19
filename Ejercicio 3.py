from abc import ABC, abstractmethod
import math

class Figura(ABC):
    @abstractmethod
    def calcular_area(self):
        pass

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return print(f"El area del circulo es: {math.pi * self.radio ** 2}")
        

class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        
    def calcular_area(self):
        return print(f"El area del rectangulo es: {self.base * self.altura}")
            

if __name__ == "__main__":
    prueba1 = Circulo(3)
    prueba2 = Rectangulo(10, 20)
    prueba1.calcular_area()
    prueba2.calcular_area()
    
