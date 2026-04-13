from vehiculo.base import Vehiculo

class Coche(Vehiculo):
    def __init__(self, marca, modelo, anio, puertas):
        super().__init__(marca, modelo, anio)
        self.puertas = puertas

    def descripcion(self) -> str:
        return f"[{self.marca} - {self.modelo}] Año: {self.anio} | Puertas: {self.puertas}"
