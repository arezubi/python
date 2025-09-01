### Conditionals ###

my_condition = False

if my_condition: ##Esto es lo mismo que if my_condition == True, es redundante ponerlo
    print("Se ejecuta la condición del if")

my_condition = 5

if my_condition == 11:
    print("Se ejecuta la condición del segundo if")

if my_condition > 10:
    print("Es mayor que 10")
else:
    print("Es menor o igual que 10")

print(my_condition)
if my_condition > 10 and my_condition < 20:
    print("Es mayor que 10 y menos que 20")
else:
    print("Es menor o igual que 10")

print("La ejecución continúa")



# 1. Escribe un programa que verifique si un nÃºmero es positivo, negativo o cero.

my_number = -4

if my_number > 0:
    print("El número es positivo")
elif my_number < 0:
    print("EL número es negativo")
else:
    print("El número es 0")
# 2. Solicita al usuario que ingrese su edad y muestra un mensaje indicando si es mayor de edad(18 aÃ±os o mÃ¡s) o menor de edad.

edad = int(input("Dime cuál es tu edad "))
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

# 3. Escribe un programa que verifique si una cadena de texto estÃ¡ vacÃ­a y muestre un mensaje en consecuencia.

texto = input("Introduce una cadena de texto: ")
if texto == '': 
    print("El cadena está vacía")
else:
    print("La cadena no está vacía")

# 4. Crea un programa que solicite dos nÃºmeros al usuario y compare cuÃ¡l es mayor. Si son iguales, muestra un mensaje indicando la igualdad.

num1 = input("Dime el primer número ")
num2 = input("Dime el segundo número ")

if num1 > num2:
    print(f"El primer número,{num1}, es mayor que el segundo, {num2}")
elif num1 < num2:
    print(f"El primer número, {num1}, es menor que el segundo, {num2}")
else:
    print(f"Los números {num1} y {num2}, son iguales")

# 5. Escribe un programa que verifique si un nÃºmero es divisible por 3 y por 5 al mismo tiempo.

num3 = int(input("Dime un núero "))

if num3 % 3 == 0 and num3 % 5 == 0:
    print(f"El número {num3} es divisible entre 3 y 5")
else:
    print(f"El número {num3} no es divisible entre 3 y 5")

# 6. Solicita al usuario que ingrese un nÃºmero y verifica si es par o impar.

num4 = int(input("Dime un número"))

if num4 % 2 == 0: 
    print(f"{num4} es par")
else: 
    print(f"{num4} es impar")

# 7. Escribe un programa que determine si una persona puede votar en funciÃ³n de su edad(mayor o igual a 18). Si tiene 16 o 17 aÃ±os, indica que puede votar con permiso especial.

edad = int(input("Dime tu edad "))

if edad >= 18:
    print("Puedes votar")
elif edad >= 16 and edad < 18:
    print("Puedes votar con permiso especial")
else: 
    print("No tienes edad para votar")

# 8. Crea un programa que solicite una contraseÃ±a al usuario y verifique si coincide con una contraseÃ±a predefinida. Si no coincide, muestra un mensaje de error.

contraseña = "hola1234"

cont = input("Escribe la contraseña ")

if contraseña == cont:
    print("Bien, las contraseñas coinciden")
else:
    print("Error! Las contraseñas no coinciden")

# 9. Escribe un programa que determine si un nÃºmero estÃ¡ entre 10 y 20 (ambos incluidos).

# 10. Escribe un programa que simule un semÃ¡foro: solicita al usuario que ingrese un color(rojo, amarillo, verde) y muestra un mensaje indicando si debe detenerse, estar alerta o avanzar.