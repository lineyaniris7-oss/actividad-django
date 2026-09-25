from empresa.empleado import empleado

class administrativo(empleado):
    def calcular_bonificacion(self):
        return self.salario * 0.10
