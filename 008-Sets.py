# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=16335

### Sets ###

# Definición - de base tiene un array - lista
#Es un tipo de dato


my_set = set()
my_other_set = {}

print(type(my_set)) #tipo de dato set
print(type(my_other_set))  # Inicialmente es un diccionario tipo de dato set


#Vamos a entenderlo inicialmente como una lista, podemos poner diferentes tipos de datos en el set
my_other_set = {"Brais", "Moure", 35}
print(type(my_other_set)) #Ahora es un set

#Lo que ocurre en la línea 10 es que hay dos tipos de datos: set y diccionario, que se pueden definir de la misma manera.
#Al definir los datos que van en el set, python ya sabe que es un set, no un diccionario

print(len(my_other_set))

# Inserción

my_other_set.add("MoureDev")

print(my_other_set)  # Un set no es una estructura ordenada, no lo ordena, es aleatorio
#NO podemos acceder a los elementos con indice

my_other_set.add("MoureDev")  # Un set no admite repetidos

print(my_other_set)

# Búsqueda

print("Moure" in my_other_set)
print("Mouri" in my_other_set)

# Eliminación

my_other_set.remove("Moure")
print(my_other_set)

my_other_set.clear()
print(len(my_other_set))

del my_other_set
# print(my_other_set) NameError: name 'my_other_set' is not defined

# Transformación

my_set = {"Brais", "Moure", 35}
my_list = list(my_set)
print(my_list)
print(my_list[0])

my_other_set = {"Kotlin", "Swift", "Python"}

# Otras operaciones

my_new_set = my_set.union(my_other_set)
print(my_new_set.union(my_new_set).union(my_set).union({"JavaScript", "C#"}))
print(my_new_set.difference(my_set))