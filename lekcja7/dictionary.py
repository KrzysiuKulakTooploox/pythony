from kwargs import print_info_about_dog

dict_a = {}
dict_b = dict()

print(dict_a)
print(dict_b)

dict_c = {
    "name": "Azorek",
    "age": 4,
    "favorite_snacks": ["chrupki łososiowe", "wątróbka"]
}

print(dict_c)
dict_c["name"] = "Tali"
print(dict_c)
dict_c["number_of_legs"] = 4
print(dict_c)

dict_c.update(
    {
        "age": 5,
        "owner": "Jakiś Pan",
        "name": "Tali"
    }
)
print(dict_c)

for item in dict_c:
    print(item)

for item in dict_c.values():
    print(item)

print(dict_c.keys())
print(dict_c.values())
print(dict_c.items())

for key, value in dict_c.items():
    if key == "name":
        print("Piesek nazywa się " + str(value))
    else:
        print("Klucz " + key + " ma wartość " + str(value))




dogs = [
    {
        "name": "Azorek",
        "age": 4,
        "breed": "Wyżeł",
        "favorite_snacks": ["chrupki łososiowe", "wątróbka"]
    },
    {
        "name": "Rex",
        "age": 14,
        "breed": "Niżeł",
        "favorite_snacks": ["szynka z chodnika"]
    },
    {
        "name": "Tali",
        "age": 13,
        "breed": "Kundel",
        "favorite_snacks": ["kości"]
    },
]

for dog in dogs:
    print_info_about_dog(dog["name"], dog["age"], dog["breed"], favorite_snacks=dog["favorite_snacks"])
