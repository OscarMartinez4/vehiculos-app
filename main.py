from vehiculo.coche import Coche
from vehiculo.moto import Moto
from gestion.inventario import Inventario
from utils.helpers import imprimir_titulo

def main():
    inventario = Inventario()

    coche1 = Coche("Toyota", "Corolla", 2020, 4)
    moto1 = Moto("Yamaha", "R6", 2019, 600)

    inventario.agregar_vehiculo(coche1)
    inventario.agregar_vehiculo(moto1)

    imprimir_titulo("Inventario de Vehículos")
    inventario.mostrar_vehiculos()

if __name__ == "__main__":
    main()
