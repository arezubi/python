'''
### Strings ###

my_variable = "Mi string"
my_other_variable = 'Mi otra string'

print(len(my_variable))
print(len(my_other_variable))

print(my_variable + ' ' + my_other_variable)

my_new_line_string = ("Esto es un string\ncon salto de linea")
print(my_new_line_string)

my_tab_string = ("\tEsto es un string con tabulación")
print(my_tab_string)

my_scape_string = ("\\tEsto es un string\\nescapado")
print(my_scape_string)

### Formateo ###

name, surname, age = "Andrés", "Reyes", 35

print("Mi nombre es {} {} y mi edad es {}".format(name, surname,age))
print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age))
print(f"Mi nombre es {name} {surname} y mi edad es {age}")

### Desempaquetado ###
language = "Python"
a, b, c, d, e, f = language

print(a)
print(e)

### División ###

language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

### Reverse ###
reversed_language = language[::-1]
print(reversed_language)

'''

# 1. Declara una variable text con la frase â€œAprendiendo Pythonâ€ y luego imprime la longitud de la cadena usando len().

text = "Aprendiendo Phyton!"
print(len(text))

# 2. Concatena dos cadenas: â€œHolaâ€ y â€œPythonâ€, y muestra el resultado en una sola lÃ­nea.
cadena, cadena2 = "Hola", "Python"
print(f"{cadena} {cadena2}")

# 3. Crea una cadena que incluya un salto de lÃ­nea, y luego imprÃ­mela para ver el resultado.
cadena = "Esto es una cadena \n con salto de línea"
print(cadena)
# 4. Usa el formateo de cadenas con f-strings para imprimir tu nombre, apellido y edad en una cadena de texto.

nombre, apellido, edad = "Andrés", "Reyes", 35
print(f"Mi nombre es {nombre} {apellido} y tengo {edad} años")

# 5. Desempaqueta los caracteres de la palabra â€œPythonâ€ en variables separadas y luego imprÃ­melos uno por uno.

a, b, c, d, e, f = "Python"
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

# 6. Extrae un â€œsliceâ€ de la palabra â€œProgramaciÃ³nâ€ para obtener los caracteres desde la posiciÃ³n 3 hasta la 7.
palabra = "Programación"
slice = palabra[3:7]
print(slice)

# 7. Invierte la cadena â€œPythonâ€ usando slicing y muestra el resultado.

cadena = "Python"
slice_reverse = cadena[::-1]
print(slice_reverse)

# 8. Convierte la cadena â€œaprendiendo pythonâ€ en mayÃºsculas usando el mÃ©todo adecuado e imprÃ­mela.

cadena = "parendiendo python"
print(cadena.upper())

# 9. Cuenta cuÃ¡ntas veces aparece la letra â€œnâ€ en la cadena â€œProgramaciÃ³n en Pythonâ€.

cadena = "Programación en Python"
print(f"La letra 'n' aparece" , cadena.count("n"), "veces")

# 10. Verifica si la cadena â€œ12345â€ es numÃ©rica usando el mÃ©todo adecuado e imprime el resultado.

cadena = "12345"
print(cadena.isnumeric())