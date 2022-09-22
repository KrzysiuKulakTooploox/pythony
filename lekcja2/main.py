# różne typy zmiennych:
zmienna_0 = 123
zmienna_1 = "123"
zmienna_2 = True
zmienna_3 = 1.23
print(type(zmienna_0))
print(type(zmienna_1))
print(type(zmienna_2))
print(type(zmienna_3))

# przykładowa lista
list_0 = [zmienna_0, zmienna_2]
print(list_0)
print(type(list_0))
list_1 = [123, 345, False]
print(list_1)

students = ["Jacek Piętka", "Alicja Piętka", "Bob Bobowski", "Andrzej Andrzejewski"]

# iteracja po liście studentów
for student in students:
    print(student + "?")
    print("Jestem!")
    if student == "Bob Bobowski":
        print("Do dyrektora!")

# sprawdzanie, czy element jest w liście
print("Bob Bobowski" in students)

print(len(students))  # sprawdzanie długości listy
print(students[-1])  # ostatni element od końca
print(students[1:4])  # list slices
print(students)
students.append("Adam Adamowski")  # dodawanie elementu na koniec listy
print(students)

# dodawanie listy do listy
students += ["Ania Annowska", "Zuza Zuzowska"]  # students = students + ["Ania Annowska"]
print(students)
# podmiana elementu w liście
students[0] = "Piotr Piotrowski"
print(students)
# usuwanie elementu listy
students.remove("Alicja Piętka")
print(students)
# wstawianie elementu na początek listy
students = ["Alicja Alicjowska"] + students
print(students)
# dodawanie listy do listy metodą extend
students.extend(["Kazimierz Kazimierski"])
print(students)

# iterowanie po stringu
kazimierz_str = "Kazimierz Kazimierski"
for letter in kazimierz_str:
    print(letter + "!")

print(len(kazimierz_str))  # sprawdzanie długości stringa
print(kazimierz_str[4:12])  # string slice

# pobieranie inputu użytkownika
user_name = input("Przedstaw się: ")
print("Cześć, " + user_name + "!")
# str() zmienia wartość innego typu (np. int) na wartość typu str
print("Twoje imie ma " + str(len(user_name)) + " liter")

user_age = input("Ile masz lat? ")
print(type(user_age))
print("za 10 lat będziesz miał: ")
# int() zmienia wartość innego typu (np. str) na wartość typu int
print(int(user_age) + 10)
