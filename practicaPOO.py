"""
class volumen:
    def __init__(self, nivelDeVolumen, bajarVolumen, limite = 10, subirVolumen=1 ):
      self.__nivelDeVolumen = nivelDeVolumen
      self.__bajarVolumen = bajarVolumen
      self.__subirVolumen = subirVolumen

    def nivelDeVolumen(self):
        if self.__nivelDeVolumen in volumen:
            pass
    def subirVolumen(self, subirVolumen):
        if self.__subirVolumen in volumen:
            self.__subirVolumen += subirVolumen
            return f"Volumen aumentado a {volumen}"
    def bajarVolumen(self, bajarVolumen):
        if self.__bajarVolumen in volumen:
            self.__bajarVolumen -= bajarVolumen
            return f"Volumen disminuido a {volumen}"
        """
class ControlVolumen:
    def __init__(self):
        self.__volumen = 5  # Nivel medio

    def ajustar_volumen(self, cambio):
        nuevo_volumen = self.__volumen + cambio
        if nuevo_volumen < 1:
            self.__volumen = 1
            return "El volumen no puede ser menor que 1. Se ajustó al mínimo."
        elif nuevo_volumen > 10:
            self.__volumen = 10
            return "El volumen no puede ser mayor que 10. Se ajustó al máximo."
        else:
            self.__volumen = nuevo_volumen
            return f"Volumen ajustado a {self.__volumen}."

    def mostrar_volumen(self):
        return f"El volumen actual es {self.__volumen}."


def menu():
    parlante = ControlVolumen()
    while True:
        print("\n--- CONTROL DE VOLUMEN ---")
        print("1. Subir volumen")
        print("2. Bajar volumen")
        print("3. Mostrar volumen actual")
        print("4. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            print(parlante.ajustar_volumen(1))
        elif opcion == "2":
            print(parlante.ajustar_volumen(-1))
        elif opcion == "3":
            print(parlante.mostrar_volumen())
        elif opcion == "4":
            print("Saliendo del programa...")
            print(parlante.mostrar_volumen())
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    menu()

