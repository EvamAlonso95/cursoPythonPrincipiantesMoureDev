mi_tupla = tuple()

brothers = ("Antonio","Marco")
sisters = ("Laura","Dora")

silbings = brothers + sisters
print(silbings)
print(type(silbings))

print(len(silbings))

parents = ("Antonio", "Begoña")
family_members = parents + silbings
print(family_members)

padres = family_members[0:2]
silbings = family_members[2:6]
print(padres)
print(type(padres))
print(silbings)

vegetables = ("pepino","calabaza","pimiento","calabacin")
frutas = ("pera","manzana","platano","fresas")
animales = ("cerdo","vaca","cordero","pescado")

food_stuff_tp = vegetables + frutas + animales
print(food_stuff_tp)
food_stuff_list =list(food_stuff_tp)


del food_stuff_tp
# print(food_stuff_tp)

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)