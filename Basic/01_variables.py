### Variables ###

my_string_variable = "My string variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_bool_variable = False
print(my_bool_variable)

# Concatenación de variables en un print
print(my_string_variable, my_int_variable, my_bool_variable)
print("Este es el valor:", my_bool_variable)

print(len(my_string_variable))

#Variable en una sola línea
name, surname, alias, edad = "Andrés", "Reyes", "Andresito", 35
print("Mi nombre es", name, surname, "y tengo", edad, "años")   

# 1. Declara y asigna valores a las siguientes variables:
# â€¢	name: una cadena que contenga tu nombre.
# â€¢	age: un nÃºmero entero que represente tu edad.
# â€¢	height: un nÃºmero flotante que represente tu altura.
# â€¢	Imprime cada variable en una lÃ­nea separada.

name = "Andrés"
age = 35
height = 1.76

print(name)
print(age)
print(height)

# 2. Convierte la variable edad de entero a cadena y concatenala con un texto que diga cuÃ¡ntos aÃ±os tienes.

age: str = str(age)
print(type(age))
print("Tengo " + age + " años")

# 3. Declara una variable booleana is_student que indique si eres estudiante o no. Usa True o False segÃºn corresponda e imprÃ­mela.

is_student = False
if is_student:
    print("Soy estudiante")
else:
    print("No soy estudiante")
print(is_student)

# 4. Usa la funciÃ³n len() para calcular cuÃ¡ntos caracteres tiene tu nombre completo, almacenado en una variable.

nombre_completo = "Andrés Reyes"
print(len(nombre_completo))

# 5. Declara tres variables en una sola lÃ­nea que representen tu nombre, apellido y ciudad de origen. Luego, imprime estos valores.

name, surname, city = "Andrés", "Reyes", "México"
print("Soy", name, surname, "y soy de", city)

# 6. Usa la funciÃ³n input() para solicitar al usuario su color favorito y almacÃ©nalo en una variable color. Luego, imprime el valor ingresado.

color = input("¿Cuál es tu color favorito? ")
print("Tu color favorito es:", color)

# 7. Declara una variable fruit e inicialÃ­zala con un valor. Luego, cambia el valor de la fruta a otro diferente y vuelve a imprimirla.

fruit = "Manzana"
fruit = "Plátano"
print(fruit)

# 8. Convierte un nÃºmero decimal, almacenado en la variable price, a un nÃºmero entero y luego imprÃ­melo.

price = 8.9
price: int= int(price)
print(price)

# 9. Declara una variable llamada address_len y almacena en ella la cantidad de caracteres de una direcciÃ³n usando la funciÃ³n len(). Imprime el resultado.
address_len = ("C/Andrés Anton, 3. Madrid")
print(len(address_len))

# 10. Usa un tipo de dato forzado para declarar una variable phone, asegurÃ¡ndote de que siempre serÃ¡ un nÃºmero. Luego, cambia su valor a un nÃºmero diferente y verifica el tipo de la variable con type().
phone = int(123456789)
phone = 987654321
print(type(phone))