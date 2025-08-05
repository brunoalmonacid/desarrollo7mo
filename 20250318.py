"""actividad 
1_escribir un programe que liste los numeris del 3 al 13
2_escribir un programe que liste los numeros pares de 2 en 2 comprendidios 
entre 10 y 20 incluidos
3_escribe un programa que liste los numeros comprendidos entre 21y31 de manera decreciente
"""
"""
actividad 1
for i in range (3,14):
    print(i)

actividad2
for i in range(10, 21, 2):
        print (i)

actividad3
for i in range(31, 20,-1):
    print(i)
"""
"""
actividades del cuadernillo pag51
1. Escribe un programa que sume todos los números de una
lista y luego responde ¿Qué tipo de variable utilizamos para
resolver?
2. Escribe un programa que imprima el cuadrado de los números del 1 al
10.
3. Escribe un programa que cuente los caracteres de una cadena de
texto proporcionada por el usuario utilizando el for.
4. Escribe un programa que cuente el número de vocales en una cadena
de texto proporcionada por el usuario.

2_for i in range(1, 11):
    print(i**2)

3_ palabra = input("palabra a contar:")
contador = 0
for i in palabra: 
    contador += 1
    print("la cantidad de caracteres de la palabra son:", i)

4_
palabras=input("paralbra para contar vocales ")
contador_vocales = 0
vocales="aeiouAEIOU"
for contador in palabras:
    if contador in vocales:
        contador_vocales+= 1
        print("las vocales son:", contador_vocales)
"""
  