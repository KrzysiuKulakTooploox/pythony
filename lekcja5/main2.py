# type hinting

def print_do_something(something: str) -> None:
    print("I'm doing " + something)


def do_something(something: str) -> str:
    return "I'm doing " + something


def add(a: int, b: int) -> int:
    return a + b


print((do_something("something stupid") + " ") * 2)
print(do_something("something great"))

print(do_something(do_something("nested something")))