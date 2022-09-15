greeting_message = "Hello world"
print(greeting_message)

var_1 = 2
var_2 = 3
var_3 = "abc"
var_4 = var_1 * var_2
print(var_4)

number_of_used_vacation_days = 23
yearly_vacation_days = 24

are_all_the_days_used = number_of_used_vacation_days == yearly_vacation_days
are_any_days_left = number_of_used_vacation_days < yearly_vacation_days
is_there_vacation_debt = number_of_used_vacation_days > yearly_vacation_days

if number_of_used_vacation_days == yearly_vacation_days:
    print("Wszystko w porządku.")
elif number_of_used_vacation_days < yearly_vacation_days:
    print("Pracownik ma niewykorzystane dni urlopowe.")
else:
    print("Pracownik wykorzystał za dużo dni urlopowych.")
print("to się już pokaże")
