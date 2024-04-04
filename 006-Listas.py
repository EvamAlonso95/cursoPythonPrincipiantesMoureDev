# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=10872

### Lists ###

# Definición

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [35, 24, 62, 52, 30, 30, 17]

print(my_list)
print(len(my_list))

my_other_list = [35, 1.77, "Brais", "Moure"]

print(type(my_list))
print(type(my_other_list))

# Acceso a elementos y búsqueda

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-4])
# Te cuenta el elemento que le pases de parametro dentro de esta lista
print(my_list.count(30))
# print(my_other_list[4]) IndexError
# print(my_other_list[-5]) IndexError

print(my_other_list.index("Brais"))

age, height, name, surname = my_other_list
print(name)

name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]
print(age)

# Concatenación

print(my_list + my_other_list)
#print(my_list - my_other_list)

# Creación, inserción, actualización y eliminación

#Inserta al final
my_other_list.append("MoureDev")
print(my_other_list)

#Inserta en la posción que le pases
my_other_list.insert(1, "Rojo")
print(my_other_list)

#Re declarar el valor
my_other_list[1] = "Azul"
print(my_other_list)

my_other_list.remove("Azul")
print(my_other_list)

#Elimina el primer elemento, no todos los que estén repetidos
my_list.remove(30)
print(my_list)

#Elimina el último elemento -> nos devuelve el valor que has eliminado
print(my_list.pop())
print(my_list)

#Eliminamos el elemento del indice 2 y lo guardamos en una variable
my_pop_element = my_list.pop(2)
print(my_pop_element)
print(my_list)

#Solo elimina y no retorna ningún elemento
del my_list[2]
print(my_list)

# Operaciones con listas

#Hace una copia de la lista
my_new_list = my_list.copy()

#Borra la lista entera
my_list.clear()
print(my_list)
print(my_new_list)

#Revierte los valores de la lista
my_new_list.reverse()
print(my_new_list)

my_new_list.sort()
print(my_new_list)

# Sublistas
# ¿¿
print(my_new_list[1:3])

# Cambio de tipo

my_list = "Hola Python"
print(my_list)
print(type(my_list))