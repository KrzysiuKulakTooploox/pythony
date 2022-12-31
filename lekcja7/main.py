tuple_a = (123, "123", "abc")
list_a = [123, "123", "abc"]

tuple_b = (123,)

print(tuple_a[1])
print(list_a[1])

for item in tuple_a:
    print(item)

for item in list_a:
    print(item)

print(id(list_a))
list_a += ["def", 456]
print(id(list_a))

print(id(tuple_a))
tuple_a += ("def", 456)
print(id(tuple_a))