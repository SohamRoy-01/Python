class Person:
    country = "India"
    def __init__(self):
        super().__init__()
        print("Initializing person...\n")
    

    def takeBreath(self):
        print("I am breathing...")


class Employee(Person):
    company = "Honda"
    def __init__(self):
        super().__init__()
        print("Initializing Employee...\n")
    def getSalary(self):
        print(f"Salary is {self.salary}")

    def takeBreath(self):
        super().takeBreath()
        print("I am an Employee So dont know when can I breath")


class Programmer(Employee):
    company = "Fiver"
    def __init__(self):
        super().__init__()
        print("Initializing Programmer...\n")

    def getSalary(self):
        print("No salary to programmers")
    def takeBreath(self):
        super().takeBreath()
        print("I am a programmer so I am breathing fine for now")

# P = Person()
# P.takeBreath()
# E = Employee()

# E.takeBreath()
pr = Programmer()
# pr.takeBreath()


