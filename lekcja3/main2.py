# dogs = ["Azor", "Reksio", "Tali"]
#
# for dog in dogs:
#     print(dog)
#     print(dogs)
#
#
# run = True
# while run:
#     decision = input("1. Dodaj psa. 2. Zakończ")
#     if decision == "1":
#         new_dog = input("Podaj imię psa: ")
#         dogs.append(new_dog)
#         print(dogs)
#     elif decision == "2":
#         run = False
# print("Zakończono działanie programu!")
#
# list_a = [""]
#
# simulation = 10000
#
# counter = 0
# while simulation > 0:
#     counter += 1
#     simulation -= 235
#
# print(counter)
#
#
list_a = ["a", "b", "c", "d"]
print(list_a[2])
print(len(list_a))
list_a.append("e")
print(list_a)

for i, element in enumerate(list_a, start=1):
    print(str(i) + ". " + element)

# str_a = "abcd"
# print(str_a[2])
# print(len(str_a))
# str_a += "efgh"
# print(str_a)
#
# for letter in str_a:
#     print(letter)

