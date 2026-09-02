class Cuenta:
    def __init__(self, numero, saldo):#constructor
        self.numero = numero
        self.__saldo = saldo
    def depositar(self, cantidad):#mètodos o comportamientos
        if cantidad > 0:
            self.__saldo += cantidad
    def retirar(self, cantidad):
        if cantidad > 0:
            self.__saldo -= cantidad

#imprimir saldo
    def imprimirsaldo(self):
        print(f"El saldo de la cuenta {self.numero} es: {self.__saldo}")

#creaciòn del objeto
cuenta1 = Cuenta(1111, 1000)
cuenta1.depositar(9999)
print(cuenta1.imprimirsaldo())