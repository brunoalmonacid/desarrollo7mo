""""
#ej POO
class Persona:
#las clases usan pascalkays, las clases simpre usan el self(solo en clases)
    def __init__(self, nombre, apellido, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
#el self siempre primero
    def saludar(self):
        return f"hola, mamhuevo soy{self.nombre}"
    
#programa 
ana = Persona("ana", "perez", "12353268")
pancho = Persona("pancho", "hernandez", "12345678")
alfonsin = Persona("alfonsin", "fernandez", "12124238")

#actividad 

class Autos: 
    def __init__(self, marca, modelo, patente, kilometraje):
        self.marca = marca
        self.modelo = modelo
        self.patente = patente
        self.kilometraje = kilometraje
    def datosAutos(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Patente: {self.patente}, Kilometraje: {self.kilometraje}"
mustang = Autos("ford", "mustang", "gal353", "10000")
ferrari = Autos("ferrari", "f40", "abc123", "5000")
bmw = Autos("BMW", "M3 E36", "jam999", "20000")
print(mustang.datosAutos())
print(ferrari.datosAutos())
print(bmw.datosAutos())

"""
#ejercicoo cuenta 
class cuenta: 
    def __init__(self, titular, numeroDeCuenta, monto=0):
        self.__titular = titular
        self.__numeroDeCuenta = numeroDeCuenta
        self.__monto = monto
       
    def get_titular(self):
        return self.__titular     
    def get_numeroDeCuenta(self):
        return self.__numeroDeCuenta    
    def get_monto(self):
        return self.__monto
    def mostrarDatos(self):
        return f"titular:{self.__titular}, numero de cuenta:{self.__numeroDeCuenta}, monto:{self.__monto}"
    def ingresarDinero(self, cantidad):
        if cantidad > 0:
            self.__monto += cantidad
            return f"Se ingresaron {cantidad}"
        else:
            return "No se puede ingresar dinero negativo"
    def retirarDinero(self, cantidad):
        if cantidad > 0:
            if cantidad <= self.__monto:
                self.__monto -= cantidad
                return f"Se retiraron ${cantidad}"
            else:
                return "No hay suficiente saldo"
            
pancho = cuenta("pancho", "12451612")
#menu hecho por gpt
def menu():
    mi_cuenta = pancho

    while True:
        print("\n--- MENÚ CUENTA BANCARIA ---")
        print("1. Crear cuenta")
        print("2. Mostrar datos de la cuenta")
        print("3. Ingresar dinero")
        print("4. Retirar dinero")
        print("5. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            titular = input("Nombre del titular: ")
            numero = input("Número de cuenta: ")
            monto = float(input("Monto inicial: "))
            mi_cuenta = cuenta(titular, numero, monto)
            print("Cuenta creada correctamente.")
        elif opcion == "2":
            if mi_cuenta:
                print(mi_cuenta.mostrarDatos())
            else:
                print("Primero debes crear una cuenta.")
        elif opcion == "3":
            if mi_cuenta:
                cantidad = float(input("¿Cuánto dinero quieres ingresar?: "))
                print(mi_cuenta.ingresarDinero(cantidad))
            else:
                print("Primero debes crear una cuenta.")
        elif opcion == "4":
            if mi_cuenta:
                cantidad = float(input("¿Cuánto dinero quieres retirar?: "))
                print(mi_cuenta.retirarDinero(cantidad))
            else:
                print("Primero debes crear una cuenta.")
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    menu()

