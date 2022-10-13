def do_something(something="walking here", number=1):
    return ("I'm doing " + something) * number


print(do_something(number=5))
print(do_something())
print(do_something("something", 2))
print(do_something(something="something else"))
