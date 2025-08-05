num1 = int(input("primer numero"))
num2 = int(input("segundo numero"))
num3 = int(input("tercer numero "))

mayor = None

if num1 >= num2:
    if num1 >= num2 and num1 >= num3:
        mayor = num1
elif num2 >= num1 and num2 >= num3:
    mayor = num2
else:
    mayor = num3


print("El número mayor es:", mayor)