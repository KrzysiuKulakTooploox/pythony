from datetime import datetime


class Project:
    def __init__(self, name, end_date):
        self.name = name
        self.end_date = end_date

    def __str__(self):
        return self.name


class FreelanceProject(Project):
    pass


class Employee:
    def __init__(self, name, project: Project | None = None):
        self.name = name
        self.project = project

    def get_general_info(self):
        general_info = f"Name: {self.name}"
        if self.project:
            general_info += f" currently working in project: {self.project}"
        return general_info


class CTO(Employee):
    def get_general_info(self):
        return f"Name: {self.name}, to on decyduje o technologi i w tym grajdołku!"


class Programmer(Employee):
    seniority_levels = ["junior", "mid", "senior"]

    def __init__(self, name, project, experience):
        super().__init__(name, project)
        if experience not in self.seniority_levels:
            raise ValueError(f"Seniority has to be one of: {self.seniority_levels}, '{experience}' given.")
        self.experience = experience

    def get_promoted(self):
        try:
            index_of_the_current_seniority = self.seniority_levels.index(self.experience)
            self.experience = self.seniority_levels[index_of_the_current_seniority + 1]
        except IndexError:
            raise ValueError("Programmer " + self.name + " already is a senior")

    def get_general_info(self):
        general_info = f"Name: {self.name}, level of experience: {self.experience}, currently working in project: {self.project}"
        return general_info

    def when_new_project_will_be_needed(self):
        return self.project.end_date


class Company:
    def __init__(self, name: str, employees: list[Employee]):
        self.name = name
        self.employees = employees

    def list_employees(self):
        for employee in self.employees:
            print(employee.get_general_info())


facebook_ads = FreelanceProject("facebook_ads", datetime.now())
Adam = Programmer("Adam", facebook_ads,"junior")
bartek = Programmer("Bartek", facebook_ads, "mid")
filip = CTO("Filip", None)
Dominik = Programmer("Dominik", Project("github", datetime.now()), "senior")
Agata = Programmer("Agata", Project("discord_bot", datetime.now()), "mid")

programmers = [Adam, bartek, Dominik, Agata]
company = Company(name="Tooploox", employees=programmers+[filip])


company.list_employees()


print("\nNow programmers will get promoted\n")

for programmer in programmers:
    try:
        programmer.get_promoted()
    except ValueError as exception:
        print(exception)
company.list_employees()
