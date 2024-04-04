# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc

### Dictionaries ###

# Definición

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

#Tipo de esctrucutra donde podemos almacenar datos de tipo clave - valor
#Los datos pueden ser de cualquier tipo
my_other_dict = {"Nombre": "Brais",
                 "Apellido": "Moure", 
                 "Edad": 35, 
                 1: "Python"}

my_dict = {
    "Nombre": "Brais",
    "Apellido": "Moure",
    "Edad": 35,
    "Lenguajes": {"Python", "Swift", "Kotlin"},
    1: 1.77
}

print(my_other_dict)
print(my_dict)

#Longuitud del diccionario
print(len(my_other_dict))
print(len(my_dict))

# Búsqueda

print(my_dict[1])
print(my_dict["Nombre"]) #Brais
print(my_dict.get("Años")) #Evitamos el error al buscar una key que no exista en el diccionario

print("Moure" in my_dict) #False
print("Apellido" in my_dict) #True porque comprueba que exista la clave no el valor

# Inserción

my_dict["Calle"] = "Calle MoureDev"
print(my_dict)


# Actualización

my_dict["Nombre"] = "Pedro"
print(my_dict["Nombre"])

# Eliminación
my_dict.pop("Nombre") #Elimina la clave que le pases
my_dict.popitem #elimina la ultima clave añadida
del my_dict["Calle"] #Elimina todo
print(my_dict)

# Otras operaciones

print(my_dict.items())#Cambia el type dict a type list
print(my_dict.keys())#Devuelve las claves en formato lista
print(my_dict.values())#Devulve los datos en formato lista
print(my_dict.clear())#Para vaciar el diccionario
print(my_dict.copy()) #Copiar 

my_list = ["Nombre", 1, "Piso"]

my_new_dict = dict.fromkeys((my_list)) #Crea un nuevo diccionario sin valores
print(my_new_dict)
my_new_dict = dict.fromkeys(("Nombre", 1, "Piso"))
print((my_new_dict))
my_new_dict = dict.fromkeys(my_dict)
print((my_new_dict))
my_new_dict = dict.fromkeys(my_dict, "MoureDev")
print((my_new_dict))

my_values = my_new_dict.values()
print(type(my_values))

print(my_new_dict.values())
print(list(dict.fromkeys(list(my_new_dict.values())).keys()))
print(tuple(my_new_dict))
print(set(my_new_dict))