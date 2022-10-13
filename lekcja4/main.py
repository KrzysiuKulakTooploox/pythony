dogs = []


def add_dog():
    new_dog = input("Jak wabi się pies: ")
    # podaj rasę
    # zapisz psa do bazy
    # sprawdź w rejestrze schroniska ...
    dogs.append(new_dog)


def print_dogs():
    for dog in dogs:
        print(dog)


while True:
    decision = input("1. dodaj psa\n2. wypisz psy\n3. zamknij\n")
    if decision == "1":
        add_dog()
    elif decision == "2":
        print_dogs()
    elif decision == "3":
        break
