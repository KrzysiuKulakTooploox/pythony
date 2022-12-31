def print_info_about_dog(name, age, breed, **kwargs):
    print("Wabi się " + name + ", ma " + str(age) + " lat, jest rasy " + breed)
    for key, value in kwargs.items():
        print("Their " + key + " is " + str(value))


# print_info_about_dog("Azor", 7, "wyżeł", owner="Samuel L. Jackson", sex="female", home="buda")
# print_info_about_dog("Rex", 17, "kundel")