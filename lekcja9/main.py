import datetime

#
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# point_dict = {"x": 1, "y": 2}
# print(point_dict["x"])
# print(point_dict["y"])
# point = Point(1, 2)
# print(point.x)
# print(point.y)
# print(type(point))


class Car:
    year_of_invention = 1886

    def __init__(self, make, year, color):
        self.make = make
        self.year = year
        self.color = color
        self.number_of_wheels = 4

    def get_age(self):
        return datetime.datetime.now().year - self.year

    @staticmethod
    def rev_engine():
        print("WRUM WRUM")

    @classmethod
    def get_invention_age(cls):
        return datetime.datetime.now().year - cls.year_of_invention



car_1 = Car("BMW", 2009, "srebrne")
car_2 = Car("BMW", 2003, "czerwone")
car_3 = Car("BMW", 2009, "srebrne")
car_4 = Car("Smart", 2018, "piaskowe")

cars = [car_1, car_2, 123, {"make": "hehe"}, car_3, car_4]
for car in cars:
    if isinstance(car, Car):
        print("Auto: ", car.make, car.color, car.get_age())
    else:
        print("to nie jest samochód!")

# car_1.rev_engine()
# print(id(car_1))
# print(car_1.color)
# car_1.color = "złote"
# print(id(car_1))
# print(car_1.color)
# print(id(car_2))

print(Car.get_invention_age())
print(car_1.get_invention_age())
print(Car.rev_engine())
print(car_1.rev_engine())


class Dog:
    def __init__(self, name, age, breed, owner=None):
        self.name = name
        self.age = age
        self.breed = breed
        self.owner = owner
        self.hunger = 0

    def bark(self):
        if self.age < 1:
            print("bork bork")
        elif self.age < 15:
            print("BORK BORK")
        else:
            print("bork")

    def get_fed(self):
        print("*cieszy się i macha ogonkiem*")
        self.hunger = 0

dog_1 = Dog("Reksio", 0.5, "labrador")
dog_2 = Dog("Tali", 16, "mieszaniec", "KK")
dog_3 = Dog("Arya", 5, "mieszaniec", "KK")

dog_2.hunger = 50
print(dog_2.hunger)
dog_2.get_fed()
print(dog_2.hunger)
#
# dog_1.bark()
# dog_2.bark()
# dog_3.bark()