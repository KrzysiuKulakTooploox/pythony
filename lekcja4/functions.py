def say_hello(name, excitement):
    print("Hello, " + name + "!" * excitement)


names = ["Michael", "Sara", "Jack"]


def load_name(id):
    return names[id]


#
# say_hello("Michael", 3)
# say_hello("Sara", 5)

# for i in range(3):
#     say_hello(load_name(i), 1)


def multiply_string(string, number):
    return string * number


def print_multiplied_string(string, number):
    print(multiply_string(string, number))


# a = multiply_string("abc", 3)
# print(a)
a = print_multiplied_string("abc", 3)
print(a)

def return_something():
    return "abc"

something = return_something

print(something())
