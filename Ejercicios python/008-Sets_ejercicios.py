it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]


#NIVEL 1
print(len(it_companies)) #7

it_companies.add("Twitter")
print(it_companies)

it_companies.update(["Shein","Temu","Kickstarter","Steam"])
print(it_companies)

it_companies.remove("Temu")
print(it_companies)

# it_companies.remove("Pepe") DA ERROR SI NO SE ENCUENTRA EN EL SET
# print(it_companies)

it_companies.discard("Pepa") #NO DA ERROR AUNQUE NO SE ENCUENTRE EN EL SET
print(it_companies)

#NIVEL 2
a_and_b = A.union(B)
print(a_and_b)

print(A.intersection(B)) #elementos en comun entre ambos sets

print(A.issubset(B)) # Si a es un subset de B
print(A.isdisjoint(B))  # si A es un disjoint de B


print(A.union(B))
print(B.union(A))

print(A.symmetric_difference(B)) #devuelve los items que no estén en ambas, que sean unicos entre ambos sets

del A
# print(A)

del (B)
# print(B)

# NIVEL 3

age_set = set(age)
print(type(age_set))

#string -> secuencia / lista de caracteres
#lista -> colección de datos ordenados que se pueden modificar
#tupla -> coleccion de datos ordenados que no se pueden modificar
#set -> colección de datos irrepetibles desordenados que sí se pueden modificar

sentence = 'I am a teacher and I love to inspire and teach people'

sentence = sentence.split()
print(sentence)

sentence = set(sentence)

print(type(sentence))
print(len(sentence))
print(sentence)