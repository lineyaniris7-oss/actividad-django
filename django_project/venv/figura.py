class figura:
    def __init__(self, largo, radio):
        self.largo = largo
        self.radio = radio

class cuadrado(figura):
    def area(self):
        resultado = self.largo * self.largo
        print(f"El area es: {resultado}")

    def perimetro(self):
        resultado = self.largo * 4
        print(f"El perimetro es: {resultado}")

class circulo(figura):
    def area(self):
        resultado = 3.1416 * self.radio * self.radio
        print(f"El area es: {resultado}")

    def perimetro(self):
        resultado = 2 * 3.1416 * self.radio
        print(f"El perimetro es: {resultado}")

circulo1 = circulo(12, 12)
circulo1.area()
circulo1.perimetro()

cuadrado1 = cuadrado(5, 10)
cuadrado1.area()
cuadrado1.perimetro()