students = []

for i in range(3):
    new_student = input("Podaj imię i nazwisko studenta: ")
    students.append(new_student)
    print(students)

for student in students:
    print(student + "?")
    print("Jestem!")
    if student == "Bob":
        print("Do dyrektora!")
