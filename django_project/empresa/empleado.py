from abc import ABC, abstractmethod

class empleado(ABC):
    def __init__(self, nombre, documento, salario): #constructor de la clase
        self.nombre = nombre #Atributo
        self.documento = documento #Atributo
        self.salario = salario #Atributo

    @abstractmethod #Mètodo abstracto
    def calcular_bonificacion(self):
        pass
    def mostrar_informacion(self):#Mètodo
        print(f"Nombre: {self.nombre}")
        print(f"Documento: {self.documento}")
        print(f"Salario: ${self.salario:,0.f}")

    def __str__(self): #Mètodo
        return f"Nombre: {self.nombre} - Documento: {self.documento}"