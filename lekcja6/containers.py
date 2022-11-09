list_a = []
# list_a = list()
list_b = [1, 2, 3, 4, 5, "a", "b"]
print(list_b[2])
print(list_b[6])
print(list_b[2:4])

print(list_a)
list_a.append(1)
print(list_a)
list_a += list_b
# list_a.extend(list_b)
print(list_a)
list_a.remove(4)
print(list_a)
list_a.remove(1)
print(list_a)
print(list_a.pop())
print(list_a)

set_a = {1, 2, 3, "a", "b", "c"}
set_a.add(4)
set_a.add(1)
print(set_a)
list_c = [1, 2, 1, 2, 3, 4, 1, 2, 3, 4]
set_b = set(list_c)
print(len(set_b))

dict_a = {"number": 123, "name": "abc", "age": 12, "is_student": True}
print(dict_a["name"])
print(dict_a["is_student"])
dict_a["gender"] = "f"
print(dict_a)
dict_a.update({"number": 125, "last_name": "def"})
print(dict_a)
print(dict_a.items())
print(dict_a.keys())
print(dict_a.values())

tuple_a = (1, 2, 3, "a")
tuple_b = (1,)
