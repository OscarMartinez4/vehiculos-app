from vehiculo.base import Vehiculo

class Coche(Vehiculo):
    def __init__(self, marca, modelo, anio, puertas):
        super().__init__(marca, modelo, anio)
        self.puertas = puertas

    def descripcion(self) -> str:
        return f"COCHE: {self.marca} {self.modelo} ({self.anio}) - {self.puertas} puertas"