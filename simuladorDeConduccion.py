
class Motor:
    def __init__(self, tipo="gasolina", potencia=100):
        self.__estado = "apagado"
        self.tipo = tipo
        self.potencia = potencia

    def encender(self):
        self.__estado = "encendido"
        print("Motor encendido.")

    def apagar(self):
        self.__estado = "apagado"
        print("Motor apagado.")

    def obtenerEstado(self):
        return self.__estado


class Transmision:
    def __init__(self, tipo="manual"):
        self.tipo = tipo
        self.marchaActual = 0

    def subirMarcha(self):
        if self.marchaActual < 5:
            self.marchaActual += 1
        print(f"Marcha actual: {self.marchaActual}")

    def bajarMarcha(self):
        if self.marchaActual > 0:
            self.marchaActual -= 1
        print(f"Marcha actual: {self.marchaActual}")

class Vehiculo:
    def __init__(self):

        self.velocidad = 0
        self.motor = Motor()
        self.transmision = Transmision()
        self.limitesVelocidad = {
            0: 0,   
            1: 20,
            2: 40,
            3: 60,
            4: 90,
            5: 120
        }

    def acelerar(self):
        if self.motor.obtenerEstado() == "encendido":
            marcha = self.transmision.marchaActual
            limite = self.limitesVelocidad.get(marcha, 0)
            if self.velocidad < limite:
                incremento = 10
                nuevaVelocidad = self.velocidad + incremento
                if nuevaVelocidad > limite:
                    self.velocidad = limite
                else:
                    self.velocidad = nuevaVelocidad
                print(f"Acelerando. Velocidad actual: {self.velocidad} km/h (Límite: {limite} km/h)")
            else:
                print(f"No se puede acelerar más. Límite de velocidad para la marcha {marcha}: {limite} km/h")
        else:
            print("El motor está apagado.")

    def frenar(self):
        if self.velocidad > 0:
            self.velocidad -= 10
            print(f"Frenando. Velocidad actual: {self.velocidad} km/h")
        else:
            print("El vehículo ya está detenido.")

    def girar(self, direccion):
        if direccion.lower() in ["izquierda", "derecha"]:
            print(f"Girando a la {direccion}.")
        else:
            print("Dirección no válida.")

    def mostrarEstado(self):
        print("ESTADO DEL VEHÍCULO")
        print(f"Velocidad: {self.velocidad} km/h")
        print(f"Motor: {self.motor.obtenerEstado()}")
        print(f"Marcha: {self.transmision.marchaActual}")

# === Menú en la terminal ===
auto = Vehiculo()

while True:
    print("--- SIMULADOR DE CONDUCCIÓN ---")
    print("1. Encender motor")
    print("2. Apagar motor")
    print("3. Acelerar")
    print("4. Frenar")
    print("5. Girar")
    print("6. Subir marcha")
    print("7. Bajar marcha")
    print("8. Mostrar estado del vehículo")
    print("9. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        auto.motor.encender()
    elif opcion == "2":
        auto.motor.apagar()
    elif opcion == "3":
        auto.acelerar()
    elif opcion == "4":
        auto.frenar()
    elif opcion == "5":
        direccion = input("¿Izquierda o derecha?: ")
        auto.girar(direccion)
    elif opcion == "6":
        auto.transmision.subirMarcha()
    elif opcion == "7":
        auto.transmision.bajarMarcha()
    elif opcion == "8":
        auto.mostrarEstado()
    elif opcion == "9":
        print("Saliendo del simulador.")
        break
    else:
        print("Opción no válida. Intenta nuevamente.")

