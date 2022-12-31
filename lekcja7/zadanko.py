def get_input():
    user_input_1 = input("Podaj pierwszą liczbę ")
    user_input_2 = input("Podaj drugą liczbę ")
    return user_input_1, user_input_2

def perform_and_record_addition(list):
    user_input_1, user_input_2 = get_input()
    result = int(user_input_1) + int(user_input_2)
    print(result)
    list.append([user_input_1, '+', user_input_2, '=', result])

def perform_and_record_subtraction(list):
    user_input_1, user_input_2 = get_input()
    result = int(user_input_1) - int(user_input_2)
    print(result)
    list.append([user_input_1, '-', user_input_2, '=', result])

list = []
print("1. dodawanie, 2. odejmowanie 3. mnożenie 4. dzielenie 5. wypisz historię operacji 6. zakończ")
stop = False
while not stop:
    decision = input("Wybierz operacje: ")
    if decision == '6':
        stop = True
    elif decision == '1':
        perform_and_record_addition(list)
    elif decision == '2':
        perform_and_record_subtraction(list)
    elif decision == '3':
        user_input_1, user_input_2 = get_input()
        result = (int(user_input_1) * int(user_input_2))
        print(result)
        list.append([user_input_1, '+', user_input_2, '=', result])
    elif decision == '4':
        user_input_1, user_input_2 = get_input()
        result = (int(user_input_1) / int(user_input_2))
        print(result)
        list.append([user_input_1, '+', user_input_2, '=', result])
    elif decision == '5':
        print(list)
