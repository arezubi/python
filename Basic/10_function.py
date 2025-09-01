### FUNCTIONS ###

def my_function():
    print("Esto es una función")

my_function()

def sum_two_values(first_number, second_number):
    print(first_number + second_number)

def sum_two_values_2(first_number, second_number):
    return first_number + second_number

sum_two_values(4,2)
my_result = sum_two_values_2(10,5)
print(my_result)

# 1. Crea una funciÃ³n llamada "personalized_greeting" que reciba un nombre como argumento e imprima "Hola, <nombre>". Si no se proporciona ningÃºn nombre, debe saludar diciendo "Hola, desconocido".

def persolinalized_greeting (nombre = "desconocido"):
    print(f"Holan {nombre}")

persolinalized_greeting()
persolinalized_greeting("Andrés")

# 2. Escribe una funciÃ³n llamada "multiply" que reciba dos nÃºmeros como argumentos y retorne el resultado de multiplicarlos.

def multiply(num1, num2):
    return num1 * num2

print(multiply(5,5))

# 3. Crea una funciÃ³n llamada "is_even" que reciba un nÃºmero entero como argumento y retorne True si es par y False si es impar.

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

print(is_even(6))

# 4. Escribe una funciÃ³n llamada "convert_to_uppercase" que reciba una cadena de texto y la retorne en mayÃºsculas.

def convert_to_uppercase(text):
    upper = text.upper()
    return upper

print(convert_to_uppercase("hola"))

# 5. Crea una funciÃ³n llamada "arbitrary_sum" que reciba un nÃºmero arbitrario de nÃºmeros como argumentos y retorne la suma de todos ellos.

def arbitrary_sum(*numbers):
    return sum(numbers)

# 6. Escribe una funciÃ³n llamada "generate_full_greeting" que reciba dos argumentos: nombre y apellido, y retorne el saludo completo "Hola, <nombre> <apellido>". Los argumentos deben ser pasados por clave.

def generate_full_gretting(fidrt_name, second_name):
    return f"Hello {fidrt_name} {second_name}"

print(generate_full_gretting("Andrés", "Reyes"))

# 7. Crea una funciÃ³n llamada "power" que reciba dos nÃºmeros: base y exponente, y retorne el resultado de elevar la base al exponente.

def power(base, exponente):
    return base ** exponente

print(power(8,2))

# 8. Escribe una funciÃ³n llamada "calculate_average" que reciba tres nÃºmeros y retorne su promedio.

def calculate_average(a, b, c):
    return (a + b + c) / 3

# 9. Crea una funciÃ³n llamada "count_characters" que reciba una cadena de texto y retorne el nÃºmero de caracteres que contiene.

def count_characters(string):
    return len(string)

# 10. Escribe una funciÃ³n llamada "display_messages" que reciba un nÃºmero indefinido de cadenas y las imprima en mayÃºsculas, una por una, tal como se hizo en el archivo proporcionado.

def display_messages(*messages):
    for message in messages:
        print(message.upper())