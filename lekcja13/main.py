class User:
    def __init__(self, name, form_of_contract, project):
        self.name = name
        self.form_of_contract = form_of_contract
        self.project = project

    def check_employees_ptos(self, user):
        return user.calculate_pto_days()

    def calculate_pto_days(self):
        return 26


class B2BEmployee(User):
    def __init__(self, name, project):
        super().__init__(name, "B2B", project)

    def calculate_pto_days(self):
        return 27


class UoPEmployee(User):
    def __init__(self, name, project):
        super().__init__(name, "UoP", project)

    def calculate_pto_days(self):
        return 28


class UZEmployee(User):
    def __init__(self, name, project):
        super().__init__(name, "UZ", project)

    def calculate_pto_days(self):
        return 10


class CustomContractEmployee(B2BEmployee):
    def __init__(self, name, project, pto_days):
        super().__init__(name, project)
        self.pto_days = pto_days

    def calculate_pto_days(self):
        return self.pto_days


class Collaborator(User):
    def __init__(self, name, project):
        super().__init__(name, "collaborator", project)

    def check_employees_ptos(self, user):
        if user.project == self.project:
            return user.calculate_pto_days()
        else:
            raise ValueError("User checked not in accessible project")


users = [
    B2BEmployee("Adam", "Proj_1"),
    B2BEmployee("Beata", "Proj_2"),
    UoPEmployee("Czarek", "Proj_1"),
    UZEmployee("Danuta", "Proj_2"),
    CustomContractEmployee("Edward", "Proj_3", 0)
]
collaborator = Collaborator("Chris", "Proj_2")


for user in users:
    print(f"{user.name} has {user.calculate_pto_days()} PTO days")

print(f"{users[0].name} sprawdził, że {users[3].name} ma {users[0].check_employees_ptos(users[3])} dni wolnych")
print(f"{collaborator.name} sprawdził, że {users[3].name} ma {collaborator.check_employees_ptos(users[3])} dni wolnych")
print(f"{collaborator.name} sprawdził, że {users[4].name} ma {collaborator.check_employees_ptos(users[4])} dni wolnych")