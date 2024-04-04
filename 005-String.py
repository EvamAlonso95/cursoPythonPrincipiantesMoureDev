# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=8643

### Strings ###

# Cómo declararlas
my_string = "Mi String"
my_other_string = 'Mi otro String'

# Longuitud
print(len(my_string))
print(len(my_other_string))
print(my_string + " " + my_other_string)

my_new_line_string = "Este es un String\ncon salto de línea"
print(my_new_line_string)

my_tab_string = "\tEste es un String con tabulación"
print(my_tab_string)

my_scape_string = "\\tEste es un String \\n escapado"
print(my_scape_string)

# Formateo

name, surname, age = "Brais", "Moure", 35
# La más recomendada:
# Además es más seguro pues se ingresan los datos que realmente necesitamos y no pueden bugearlo
print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %d" % (name, surname, age))

# La menos recomendada:
print("Mi nombre es " + name + " " + surname + " y mi edad es " + str(age))

# Inferencia de datos: Esto si no estamos formateando es la ideal
print(f"Mi nombre es {name} {surname} y mi edad es {age}")

# Desempaqueado de caracteres

language = "python"
a, b, c, d, e, f = language
print(a)
print(e)

# División
#no cuenta el 3
language_slice = language[1:3]
print(language_slice)

#te imprime todo desde esa posicion
language_slice = language[1:]
print(language_slice)

#Te cuenta desde el final
language_slice = language[-2]
print(language_slice)

#Por separado
language_slice = language[0:6:2]
print(language_slice)

# Reverse

reversed_language = language[::-1]
print(reversed_language)

# Funciones del lenguaje

print(language.capitalize())
print(language.upper())
# Cuantos caracteres hay
print(language.count("t"))
print(language.isnumeric())
print("1".isnumeric())
print(language.lower())
# isupper comprueba si estan en mayus
print(language.lower().isupper())
print(language.startswith("Py"))
print("Py" == "py")  # No es lo mismo