from empresa.empleado import empleado

class gerente (empleado):
    def calcular_bonificacion(self):
        return self.salario * 0.20