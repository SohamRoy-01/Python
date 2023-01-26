class Person:
    country = "India"

    def takeBreath(self):
        print("I am breathing...")


class Employee(Person):
    company = "Honda"

    def getSalary(self):
        print(f"Salary is {self.salary}")

    def takeBreath(self):
        print("I am an Employee So dont know when can I breath")


class Programmer(Employee):
    company = "Fiver"

    def getSalary(self):
        print("No salary to programmers")


P = Person()
P.takeBreath()
E = Employee()

E.takeBreath()
pr = Programmer()
pr.takeBreath()