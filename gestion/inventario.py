class Inventario:
    def __init__(self):
        self.vehiculos = []

    def agregar_vehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)

    def mostrar_vehiculos(self):
        for v in self.vehiculos:
            print(v.descripcion())
