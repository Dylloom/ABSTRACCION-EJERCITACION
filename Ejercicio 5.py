from abc import ABC, abstractmethod
import math

class Empleado(ABC):
    @abstractmethod
    def calcular_sueldo(self):
        pass

class EmpleadoPorHora(Empleado):
    def __init__(self, nombre, Phora, horas):
        self.nombre = nombre
        self.Phora = Phora
        self.horas = horas

    def calcular_sueldo(self):
        return print(f"Al empleado {self.nombre} se le pagan {self.Phora} por hora y a trabajado {self.horas} se le pagara {self.horas * self.Phora}")
        

class EmpleadoFijo(Empleado):
    def __init__(self, nombre, sueldo):
        self.nombre = nombre
        self.sueldo = sueldo
        
    def calcular_sueldo(self):
        return print(f"Al empledo {self.nombre} se le pago el sueldo de {self.sueldo}")
            

if __name__ == "__main__":
    prueba1 = EmpleadoPorHora("Juan", 10, 40)
    prueba2 = EmpleadoFijo("Mike", 500)
    prueba1.calcular_sueldo()
    prueba2.calcular_sueldo()
