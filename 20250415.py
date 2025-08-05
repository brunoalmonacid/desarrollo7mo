def nombres (a):
    
    return (f"hola {a}, como estas")
    
print(nombres("pancho"))


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5)) 

 
def dividir(a,b):
    if a/b == 0:
        return "no se puede dividir por 0"
    else:
        return a/b
def multiplicar(a,b):
    if a*b:
        return a*b
def restar(a,b):
    if a-b:
        return a-b
def sumar(a,b):
    if a+b:
        return a+b
def menu():
    while True:
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")
if opcion == "1":
            a = int(input("Ingrese el primer número: "))
            b = int(input("Ingrese el segundo número: "))
            print(f"Resultado: {sumar(a, b)}")+