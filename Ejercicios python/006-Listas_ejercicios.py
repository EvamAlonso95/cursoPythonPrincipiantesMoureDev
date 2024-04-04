my_list = list()
print(my_list)

my_list =["Eva","Alonso",28,"Rojo",1995]

print(len(my_list))


firts_item = my_list[0]
middle_item = my_list[2]
last_item = my_list[-1]

print(firts_item,middle_item,last_item)

mixed_data_types = list()
mixed_data_types = ["Eva",28,"1.60","in a relationship","Spain"]

it_companies = [ "Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle","Amazon"]
print(it_companies)

print('Compañías:', it_companies)
print('Número de compañías:', len(it_companies))

# it_companies[4] = "Xiaomi"
# print(it_companies)

print(it_companies[2].upper())

# 14 ni puta idea

does_exits = 'Oracle' in it_companies
print(does_exits)

# it_companies.reverse()
# print(it_companies)

# del it_companies[0:3]
# print(it_companies)
# CUIDADO no elimina los indices que marcas
# del it_companies[3:7]
# print(it_companies)

# del it_companies[2]
# print(it_companies)

# Ordena alfabeticamente
it_companies.sort()
print(it_companies)

#Lo ordena al revés
it_companies.sort(reverse=True)
print(it_companies)

it_companies.clear()
print(it_companies)

# del it_companies
# print(it_companies)


front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack = front_end + back_end
print(full_stack)

full_stack.insert(5, "Python")
print(full_stack)
full_stack.insert(6, "SQL")
print(full_stack)

## DIFILES
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()
print(ages)

min_age = ages[0]
max_age = ages[-1]

print("La edad mínima es:",min_age)
print("La edad máxima es:",max_age)

items = len(ages)
middle = items / 2
print(middle)

sum = sum(ages)
average_age = sum/len(ages)
print(average_age)


countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]

lengt_countries = len(countries)
print(lengt_countries)

middle_country = lengt_countries / 2

print(middle_country)

print(countries[97])


# print(countries[middle_country])


mitad_primera = countries[:len(countries)//2]
# print(mitad_primera)

mitad_segunda = countries[len(countries)//2:]
# print(mitad_segunda)


mitad = countries[len(countries)//4:len(countries)*3//4]
print(mitad)
