class Pet:
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner

    def get_fed(self):
        print("mmm ale pyszne!")


class Spider(Pet):
    def __init__(self, name, owner, moult):
        super().__init__(name, owner)
        self.moult = moult

    def get_fed(self):
        super().get_fed()
        print("robale!")

    def __str__(self):
        return self.name + ", przeszedł " + str(self.moult) + " wylinek, należy do " + self.owner


class Dog(Pet):
    def __init__(self, name, owner, age):
        super().__init__(name, owner)
        self.age = age

    def __str__(self):
        return self.name + ", ma " + str(self.age) + " lat, należy do " + self.owner


class Labrador(Dog):
    def get_fed(self):
        print("dawaj dawaj więcej żarcia!")

    def __str__(self):
        return super().__str__() + ", jest labradorem"

dog = Dog("Tali", "Krzysiu", 13)
spider = Spider("Silvestr", "Krzysiu", 10)
dog_2 = Dog("Arya", "Krysia", 9)
dog_3 = Labrador("Kawa", "Jakaś pani z wybiegu dla psów", 5)

print(dog_2)
print(dog_3)
dog.get_fed()
dog_3.get_fed()

print(type(dog))
print(type(dog_3))
print(type(spider))


def pet_a_dog(pet):
    if isinstance(pet, Dog):
        print("pat pat, " + pet.name + " jaki dobry piesek")
    else:
        print("Zabierzcie mnie to!")

pet_a_dog(dog)
pet_a_dog(spider)
pet_a_dog(dog_3)
