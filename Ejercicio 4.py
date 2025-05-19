from abc import ABC, abstractmethod
import math

class Notificacion(ABC):
    @abstractmethod
    def enviar(self):
        pass

class Email(Notificacion):
    def __init__(self, email):
        self.email = email

    def enviar(self):
        return print(f"El email: {self.email} envio un correo")
        

class Rectangulo(Notificacion):
    def __init__(self, numero):
        self.numero = numero
        
    def enviar(self):
        return print(f"El numero: {self.numero} envio un mensaje")
            

if __name__ == "__main__":
    prueba1 = Email("Prueba@gmail.com")
    prueba2 = Rectangulo("12 3456-7890")
    prueba1.enviar()
    prueba2.enviar()
