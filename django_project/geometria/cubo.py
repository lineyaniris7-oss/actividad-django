from figura import figura

class cubo(figura):
    
    def __init__(self, largo):
        self.largo = largo
    
    def calcular_volumen(self):
        return self.largo ** 3

    def mostrar(self):
        volumen = self.calcular_volumen()
        print(f"El volumen del cubo es: {volumen}")