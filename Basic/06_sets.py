### SETS ###

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) #Inicialmente es un diccionario

my_other_set = {"Andrés", "Reyes", 35}
print(type(my_other_set))

print(len(my_other_set))

my_other_set.add("Zubikarai")
print(my_other_set) #Un set no es una estructura ordenada

my_other_set.add("Zubikarai")
print(my_other_set) #Un set no admite duplicados

