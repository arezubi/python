### LOOPS / BUCLES ###

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 1
else: #Es opcional
    print("Mi condición es >= 10")

print("Continuamos con la ejecución")

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Mi condición es 15")

    print(my_condition)
print("____EJERCICIOS______")
# 1. Usa un bucle while para imprimir los nÃºmeros del 1 al 10.

numero = 1
while numero <= 10:
    print(numero)
    numero +=1


# 2. Usa un bucle for para recorrer la lista[10, 20, 30, 40, 50] e imprime cada nÃºmero.

lista = [10, 20, 30, 40, 50]

for num in lista:
    print(num)

# 3. Escribe un programa que use un bucle while para sumar los nÃºmeros del 1 al 100 e imprime el resultado.

i = 1
sum = 0
while i <= 100:
    sum += i
    i += 1
print(sum)

# 4. Escribe un bucle for que imprima cada carÃ¡cter de la cadena "Python".

cadena = "Python"

for letra in cadena:
    print(letra)

# 5. Usa un bucle while para encontrar el primer nÃºmero divisible por 7 entre 1 y 50.

i = 1
while i <= 50:
    if i % 7 == 0:
        print(i)
        break
    i += 1

# 6. Usa un bucle for para recorrer el diccionario {"name": "Brais", "age": 37, "country": "Galicia"} e imprime las claves.

dic = {"name": "Brais", "age": 37, "country": "Galicia"}

for clave in dic:
    print(clave)

# 7. Escribe un programa que use un bucle while para imprimir los nÃºmeros pares entre 1 y 20.

i = 1
while i <= 20:
    if(i % 2 == 0):
        print(i)
    i += 1

# 8. Usa un bucle for con la funciÃ³n range() para imprimir los nÃºmeros del 1 al 10 en orden inverso.

for i in range(10, 0, -1):
    print(i)

# 9. Escribe un programa que use un bucle for para contar cuÃ¡ntas veces aparece el nÃºmero 30 en la lista[30, 10, 30, 20, 30, 40].

lista = [30, 10, 30, 20, 30, 40]
count = 0

for number in lista:
    if number == 30:
        count += 1
print(count)

# 10. Usa un bucle for para recorrer una lista de nombres y detener el bucle cuando se encuentre el nombre "Brais".

names = ["Sara", "Brais", "Pedro"]

for name in names:
    if name == "Brais":
        print(f"Se ha encontrado el nombre {name}")
        break
    print(name)

for i in range(3):
    print(i)