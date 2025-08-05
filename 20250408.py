"""
1. Escribe un programa que administre el inventario de una
tienda. El programa debe permitir agregar nuevos
productos, actualizar las cantidades de los productos
existentes, y mostrar el inventario actual.

2. Escribe un programa que permita llevar un registro de
las calificaciones de varios estudiantes. El programa
debe permitir agregar estudiantes con sus
calificaciones, actualizar las calificaciones de un
estudiante existente y mostrar el promedio de
calificaciones de un estudiante específico.
"""
"""# Programa para administrar el inventario de una tienda

# Diccionario para almacenar el inventario
inventario = {}

def agregar_producto(nombre, cantidad):

    if nombre in inventario:
        print(f"El producto '{nombre}' ya existe en el inventario.")
    else:
        inventario[nombre] = cantidad
        print(f"Producto '{nombre}' agregado con cantidad {cantidad}.")

def actualizar_producto(nombre, cantidad):
    if nombre in inventario:
        inventario[nombre] += cantidad
        print(f"Producto '{nombre}' actualizado. Nueva cantidad: {inventario[nombre]}.")
    else:
        print(f"El producto '{nombre}' no existe en el inventario.")

def mostrar_inventario():
    if not inventario:
        print("El inventario está vacío.")
    else:
        print("Inventario actual:")
        for producto, cantidad in inventario.items():
            print(f"- {producto}: {cantidad}")

# Menú principal
def menu():
    while True:
        print("\n--- Menú de Inventario ---")
        print("1. Agregar producto")
        print("2. Actualizar producto")
        print("3. Mostrar inventario")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad: "))
            agregar_producto(nombre, cantidad)
        elif opcion == "2":
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad a agregar o restar: "))
            actualizar_producto(nombre, cantidad)
        elif opcion == "3":
            mostrar_inventario()
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecutar el programa
if __name__ == "__main__":
    menu()
    """

# Diccionario para almacenar los alumnos y sus notas
alumnos = {}
materias = ["Matemáticas", "Ciencias", "Historia", "Lengua"]

def agregar_alumno(nombre):
    """Agrega un nuevo alumno al registro."""
    if nombre in alumnos:
        print(f"El alumno '{nombre}' ya está registrado.")
    else:
        alumnos[nombre] = []
        print(f"Alumno '{nombre}' agregado.")

def agregar_nota(nombre, nota):
    """Agrega una nota a un alumno existente."""
    if nombre in alumnos:
        alumnos[nombre].append(nota)
        print(f"Nota {nota} agregada al alumno '{nombre}'.")
    else:
        print(f"El alumno '{nombre}' no está registrado.")

def mostrar_notas(nombre):
    """Muestra las notas de un alumno."""
    if nombre in alumnos:
        if alumnos[nombre]:
            print(f"Notas de '{nombre}': {', '.join(map(str, alumnos[nombre]))}")
        else:
            print(f"El alumno '{nombre}' no tiene notas registradas.")
    else:
        print(f"El alumno '{nombre}' no está registrado.")

def promedio_notas(nombre):
    """Calcula y muestra el promedio de notas de un alumno."""
    if nombre in alumnos:
        if alumnos[nombre]:
            promedio = sum(alumnos[nombre]) / len(alumnos[nombre])
            print(f"El promedio de notas de '{nombre}' es: {promedio:.2f}")
        else:
            print(f"El alumno '{nombre}' no tiene notas para calcular el promedio.")
    else:
        print(f"El alumno '{nombre}' no está registrado.")

# Menú principal
def menu_alumnos():
    while True:
        print("\n--- Menú de Alumnos ---")
        print("1. Agregar alumno")
        print("2. Agregar nota a un alumno")
        print("3. Mostrar notas de un alumno")
        print("4. Mostrar promedio de un alumno")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del alumno: ")
            agregar_alumno(nombre)
        elif opcion == "2":
            nombre = input("Ingrese el nombre del alumno: ")
            nota = float(input("Ingrese la nota: "))
            agregar_nota(nombre, nota)
        elif opcion == "3":
            nombre = input("Ingrese el nombre del alumno: ")
            mostrar_notas(nombre)
        elif opcion == "4":
            nombre = input("Ingrese el nombre del alumno: ")
            promedio_notas(nombre)
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecutar el programa
if __name__ == "__main__":
    menu_alumnos()