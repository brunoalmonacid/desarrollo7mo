#primer actividad 
numero = 10
while numero >= 1:
    print(numero)
    numero -= 1

#segunda actividad
numero2 = int(input("numero que se quiere saber el factorial"))
contador = 1
factorial = 1
while contador <= numero2:
    factorial *= contador 
    contador += 1 

print(f"el factorial de {numero2} es {factorial}")
#tercera actividad
