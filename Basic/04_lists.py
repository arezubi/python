### Lists ###
'''
my_list = list()
my_other_list= []

print(len(my_list))

my_list = [35, 24, 62, 52, 30, 30, 17]

print(my_list)
print(len(my_list))

my_other_list = [35, 1.77, "Andrés", "Reyes"]
print(type(my_other_list))

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1]) #Leer el último
print(my_other_list[-4])
print(my_list.count(30))
#print(my_other_list[4]) IndexError
#print(my_other_list[-5]) IndexError

age, height, name, surname = my_other_list
print(age)

my_other_list.append("AndreReyes")
print(my_other_list)

my_other_list.insert(0, "México")
print(my_other_list)

my_other_list.remove("México")
print(my_other_list)

my_list.remove(30)
print(my_list)

my_list.pop()
print(my_list)
print(my_list.pop(2))
my_pop_element = my_list.pop(2)

del my_list[2]
print(my_list)
'''

# 1. Crea una lista con los números del 1 al 5 e imprímela.

list = [1, 2, 3, 4, 5]
print(list)

# 2. Accede e imprime el tercer elemento de la lista [10, 20, 30, 40, 50].

list2 = [10, 20, 30, 40, 50]
print(list2[2])

# 3. Agrega el número 6 al final de la lista [1, 2, 3, 4, 5] e imprímela.

list.append(6)
print(list)

# 4. Inserta el número 15 en la posición 2 de la lista [10, 20, 30, 40, 50].

list2.insert(2, 15)
print(list2)

# 5. Elimina el primer valor 30 de la lista [10, 20, 30, 30, 40, 50].

list3 = [10, 20, 30, 30, 40, 50]
list3.remove(30)
print(list3)

# 6. Usa la función pop() para eliminar el último elemento de la lista [1, 2, 3, 4, 5] y almacénalo en una variable. Imprime la variable y la lista.

my_pop_list = list.pop()
print(my_pop_list)
print(list)

# 7. Invierte la lista [100, 200, 300, 400, 500] e imprímela.

list3 = [100, 200, 300, 400, 500]
list3.reverse()
print(list3)

# 8. Ordena la lista [3, 1, 4, 2, 5] en orden ascendente e imprímela.

list4 = [3, 1, 4, 2, 5]
list4.sort()
print(list4) 

# 9. Concatena las listas [1, 2, 3] y [4, 5, 6] y almacena el resultado en una nueva lista. Imprime la lista resultante.

list = [1, 2, 3]
list2 = [4, 5, 6]

list.extend(list2)
print(list)

# 10. Crea una sublista con los elementos de la lista [10, 20, 30, 40, 50] que van desde la posición 1 hasta la 3 (sin incluir la posición 3).
list = [10, 20, 30, 40, 50]
new_list = list[1:3]
print(new_list)