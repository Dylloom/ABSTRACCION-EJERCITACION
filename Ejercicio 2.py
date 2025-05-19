from abc import ABC, abstractmethod
import math

class Pago(ABC):
    @abstractmethod
    def procesar_pago(self):
        pass

class TarjetaCredito(Pago):
    def __init__(self, numero, saldo):
        self.numero = numero
        self.saldo = saldo

    def procesar_pago(self, monto):
        if self.saldo >= monto:
            self.saldo -= monto
            return print(f"Pago de {monto} procesado con tarjeta: {self.numero}, Saldo final: {self.saldo}")
        else:
            return print("Error el monto es mayor que el saldo de la tarjeta")

class PayPal(Pago):
    def __init__(self, correo, saldo):
        self.correo = correo
        self.saldo = saldo
    def procesar_pago(self, monto):
        if monto <= self.saldo:
            self.saldo -= monto
            return print(f"Pago de {monto} procesado con PayPal: {self.correo}, Saldo final: {self.saldo}")
        else:
            return print("Su saldo en PayPal es inferior al monto ingresado")
            

if __name__ == "__main__":
    prueba1 = TarjetaCredito("1234-4567-8901-2235", 100)
    prueba2 = PayPal("ElonMusk@gmail.com", 200)
    prueba1.procesar_pago(100)
    prueba2.procesar_pago(200)
    prueba1.procesar_pago(100)
    prueba2.procesar_pago(200)
