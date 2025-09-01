### Tuples ###

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (35, 1.77, "Andrés", "Reyes")
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
#print(my_tuple[4]) #IndexError
#print(my_tuple[-6]) #IndexError

print(my_tuple.count("Reyes"))
print(my_tuple.index("Reyes"))

# 1. Crea una tupla con los valores (10, 20, 30, 40, 50) e imprí­mela.

my_taple1 = (10, 20, 30, 40, 50)
print(my_taple1)

# 2. Accede al segundo elemento de la tupla (100, 200, 300, 400, 500) y muéstralo.

print(my_taple1[1])

# 3. Intenta modificar el primer elemento de la tupla (1, 2, 3) a 10 y observa el resultado.

my_tuple = (1,2,3)
#my_tuple[0] = 10 TypeError: 'tuple' object does not support item assignment


# 4. Cuenta cuÃ¡ntas veces aparece el nÃºmero 3 en la tupla (1, 2, 3, 3, 4, 5, 3).

my_tuple = (1, 2, 3, 3, 4, 5, 3)
print(my_tuple.count(3))

# 5. Encuentra el Ã­ndice de la primera apariciÃ³n de la cadena "Python" en la tupla ("Java", "Python", "JavaScript", "Python").

my_tuple = ("Java", "Python", "JavaScript", "Python")
print(my_tuple.index("Python"))

# 6. Concatena dos tuplas: (1, 2, 3) y (4, 5, 6) e imprime la tupla resultante.

my_tuple = (1,2,3)
my_tuple_2 = (4,5,6)
result = my_tuple + my_tuple_2
print(result)

# 7. Crea una subtupla con los elementos desde la posiciÃ³n 2 hasta la 4 (sin incluir la 4) de la tupla (10, 20, 30, 40, 50).

my_tuple = (10, 20, 30, 40, 50)
print(my_tuple[2:4])

# 8. Convierte la tupla ("rojo", "verde", "azul") en una lista, cambia el segundo elemento a "amarillo" y vuelve a convertirla en una tupla. Imprime la tupla resultante.

my_tuple = ("rojo", "verde", "azul")
my_list = list(my_tuple)
my_list = ("rojo", "amarillo", "azul")
my_tuple = tuple(my_list)
print(my_tuple)

# 9. Elimina una tupla llamada my_tuple usando del y luego intenta imprimirla para ver el resultado.

del my_tuple
#print(my_tuple) NameError: name 'my_tuple' is not defined

# 10. Crea una tupla con un solo elemento (el nÃºmero 100) e imprÃ­mela. AsegÃºrate de usar la sintaxis correcta para crear una tupla con un solo elemento.

my_tuple = (100, )
print(type(my_tuple))
