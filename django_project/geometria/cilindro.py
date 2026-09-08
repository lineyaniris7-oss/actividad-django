from figura import figura

class cilindro(figura):

    def __init__(self, radio, altura):
        self.radio = radio
        self.altura = altura
    
    def calcular_volumen(self):
        return 3.1416 * self.radio ** 2 * self.altura
    
    def mostrar(self):
        volumen = self.calcular_volumen()
        print(f"El volumen del cilindro es: {volumen}")