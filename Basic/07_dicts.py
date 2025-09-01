### Dictionaries ###

# 1. Crea un diccionario con las claves name, age, y country, asignando valores a cada una. Imprime el diccionario.

dict = {"name": "Andrés", "age": 36, "country": "Spain"}
print(dict)


# 2. Accede al valor de la clave name en el diccionario.

print(dict["name"])

# 3. AÃ±ade una nueva clave job con el valor "Programador" al diccionario del punto anterior. Imprime el diccionario actualizado.

dict = {"name": "Andrés", "age": 36, "country": "Spain", "job": "Programador"}
print(dict)

# 4. Modifica el valor de la clave age en el diccionario para que sea 38. Imprime el diccionario actualizado.

dict["age"] = 38
print(dict)

# 5. Elimina la clave country del diccionario e imprime el diccionario resultante.

del dict["country"]
print(dict)

# 6. Crea un diccionario donde las claves sean nÃºmeros del 1 al 5 y los valores sean sus cuadrados (ejemplo: 1: 1, 2: 4, ...).

other_dict = {1:1, 2:4, 3:9, 4:16, 5:25}
print(other_dict)

squares = {x: x**2 for x in range(1, 6)}
print(squares)


# 7. Verifica si la clave age estÃ¡ presente en el diccionario {"name": "Brais", "age": 37, "country": "Galicia"}.

print("age" in dict)

# 8. Imprime solo las claves del diccionario.

print(dict.keys())

# 9. Convierte las claves del diccionario en una lista e imprime la lista resultante.

print(list(dict))

# 10. Crea un nuevo diccionario a partir de una lista de claves ["name", "age", "job"] usando fromkeys(), asignando a todas las claves el valor "Desconocido".

my_keys = ["name", "age", "job"]
my_new_dict = dict.fromkeys(my_keys, "Desconocido")
print(my_new_dict)

print(my_new_dict.values())