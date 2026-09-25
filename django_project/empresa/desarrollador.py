from empresa.empleado import empleado

class desarrollador (empleado):
    def calcular_bonificacion(self):
        return self.salario * 0.15