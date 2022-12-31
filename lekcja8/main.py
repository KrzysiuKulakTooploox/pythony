def divide_12(value):
    result = 12 / int(value)
    print(result)
    return result


users_input = input("Podaj liczbę")
try:
    print("Jestem przed błędem!")
    divide_12(users_input)
    print("Jestem po błędzie!")
except ValueError:
    print("Podaj poprawną liczbę!")
except ZeroDivisionError:
    print("Nie można dzielić przez zero!")
print("Dalej sobie działam")

