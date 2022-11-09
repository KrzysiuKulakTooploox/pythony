stop = False
while not stop:
    decision = input("Podaj wartość 'decision', lub napisz 'stop' by zatrzymać: ")
    if decision == "stop":
        stop = True
    else:
        decision = int(decision)
        if decision > 1:
            print("Decision is greater than 1")
        elif decision == 1:
            print("Decision is equal to 1")
        else:
            print("Decision is lesser than 1")