list_a = [1, 2, 3, "abc", "def", True, False, None]

for item in list_a:
    print(str(item) + "!")
    if isinstance(item, int):
        print("jest to liczba!")
        if item == 2:
            print("Znalazłem dwójkę!")
    else:
        print("Nie jest to liczba!")


dogs = ["Azor", "Tali", "Bubuś"]
actions = ["Umyto sierść", "Obcięto pazurki", "Dano przysmaczek"]

for dog in dogs:
    print("Zajmuję się psem: " + dog)
    for action in actions:
        print("Wykonano: " + action)