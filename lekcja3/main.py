# dogs = []
# Pozwól użytkownikowi dodać trzy imiona psów (jedno po drugim) do listy dog  (użyj funkcji input).
# Na końcu programu użyj funkcji print by napisać, ile psów znajduje się na liście.
# Pod spodem umieść linijkę kodu:
# print(dogs)
# by sprawdzić, czy psy zostały odpowiednio dodane.
# Dla psów Azor, Burek i Reksio powinno się wyświetlić konkretnie:
# ['Azor', 'Burek', 'Reksio']
# Uwaga:
# Znaki wokół wydrukowanych imion są istotne.
# ['Azor, Burek, Reksio'] , albo Azor, Burek, Reksio  to niepoprawne wyniki. (edited)

# dogs = []
# dog_1 = input("Dadaj imie pierwszego psa.")
# dogs.append(dog_1)
# print("Dziękuję.")
# dog_2 = input("Podaj imie drugiego psa.")
# dogs.append(dog_2)
# print("Dziękuję.")
# dog_3 = input("Podaj imie trzeciego psa.")
# dogs.append(dog_3)
# print(dogs)
# print(len(dogs))

# Próbowałam zrobić pętle, ale mi sie nie udało :)

dogs = []
print(dogs)
n = input('Dodaj imie psa ablo napisz:"Nie"')
dogs.append(n)

k = input("Dodaj imie")
for k in dogs:
    dogs += [k]
    print(dogs)
# if k == "Nie":
#     print(len(dogs))
#     print(dogs)
#
# n = input("Dadaj imie psa.")
# for dogs = n:
#     print(dogs)
# print(len(dogs))

dogs = []
for i in range(3):
    dog_name = input('Dodaj imie psa ablo napisz:"Nie"')
    if dog_name != "Nie":
        dogs.append(dog_name)
    print(dogs)

for dog in dogs:
    print("Jaki piękny piesek!")
