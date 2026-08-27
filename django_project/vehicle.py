class vehicle:
    def __init__(self, brand, color, plate):
        self.brand = brand
        self.color = color
        self.plate = plate
        self.speed = 0
    def acelerar(self):
        self.speed += 10
        print(f"El {self.brand} aceleró a {self.speed} km/h")
    def desacelerar(self):
            self.speed -= 10
            print(f"El {self.brand} desacelero a {self.speed} km/h")


#Creación de los objetos
my_vehicle = vehicle('Hiunday', 'black', 'A7929')
my_vehicle.acelerar()
my_vehicle.acelerar()
my_vehicle.desacelerar()
my_vehicle.desacelerar()
my_vehicle.desacelerar()

#Agregar el atributo placa(plate)
#Agregar el método desacelerar 
#Subir a git en el mismo repositorio de ayer.
