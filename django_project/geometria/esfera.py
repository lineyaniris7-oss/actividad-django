from figura import figura

class esfera(figura):

    def __init__(self, radio):
        self.radio = radio

    def calcular_volumen(self):
        return (4 / 3) * 3.1416 * self.radio ** 3

    def mostrar(self):
        volumen = self.calcular_volumen()
        print(f"El volumen de la esfera es: {volumen}")