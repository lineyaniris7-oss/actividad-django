from abc import ABC, abstractmethod

class figura(ABC):
    @abstractmethod
    def calcular_volumen(self):
        pass
    def mostrar(self):
        print(f"(self.__class__.__name__) volumen: (self.calcular_volumen():.2f)")