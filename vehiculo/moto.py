from vehiculo.base import Vehiculo

class Moto(Vehiculo):
    def __init__(self, marca, modelo, anio, cilindrada):
        super().__init__(marca, modelo, anio)
        self.cilindrada = cilindrada

    def descripcion(self):
        return f"{super().descripcion()} - {self.cilindrada}cc"
