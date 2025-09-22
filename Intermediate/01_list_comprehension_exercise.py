# 1. Genera una lista utilizando comprensión con los números del 0 al 10.

my_list = [i for i in range(11)]
print(my_list)

# 2. Crea una lista utilizando comprensión con los cuadrados de los números del 1 al 10.

my_list = [i ** 2 for i in range(1,11)]
print(my_list)

# 3. Genera una lista utilizando comprensión con los números pares del 0 al 20.

my_list = [i for i in range(21) if i % 2 == 0]
print(my_list)

# 4. Convierte una lista de temperaturas en Celsius a Fahrenheit utilizando comprensión.

temperature = [20, -5, 18, 34, 23, 15]

def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

my_list = [convert_celsius_to_fahrenheit(i) for i in temperature]
print(my_list)


# 5. Crea una lista utilizando comprensión con los caracteres de una cadena.

cadena = "mi cadena"

my_list = [i for i in cadena]
print(my_list)

# 6. Filtra una lista de palabras y deja solo las que tienen más de 4 letras utilizando comprensión.

my_list = ["hola", "si", "no", "tarde", "espialidoso"]
my_list = [i for i in my_list if len(i) >= 4]
print(my_list)

# 7. Aumenta en 5 cada número de una lista con comprensión usando una función externa.

def sum_five(number):
    return number + 5

my_list = [sum_five(i) for i in range(8)]
print(my_list)


# 8. Crea una lista de booleanos que indique si cada número es mayor que 10 utilizando comprensión.

my_list = [i > 10 for i in range(11)]
print(my_list)

# 9. Multiplica solo los números impares por 3 en una lista utilizando comprensión.

my_list = [i * 3 for i in range(11) if i % 2 != 0]
print(my_list)

# 10. Usa comprensión de listas anidada para generar una matriz 3x3 con números del 1 al 9.

matrix = [[row * 3 + col + 1 for col in range(3)] for row in range(3)]
print(matrix)
