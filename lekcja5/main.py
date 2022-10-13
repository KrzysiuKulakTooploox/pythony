names = ["Alice", "Bob", "Charlie"]
dog_names = ["Fafik", "Taluś", "Bubuś"]

print("jestem przed pętlą")
print(names)
for name in names:
    print("wchodzę do pętli")
    print("wewnątrz tego obiegu pętli name ma wartość " + name)
    print("wewnątrz pętli names ma wartość " + str(names))

print("poza pętlą")

for name in dog_names:
    print("wewnątrz psiej pętli")
    print(name)


print("jestem poza pętlą!")
