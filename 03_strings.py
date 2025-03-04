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
