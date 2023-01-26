from tkinter import E


class Employee:  # Parental
    company = "google"

    def showDetails(self):
        print("This is an employee")

class Programmer(Employee):  # overwrite
    lang = "Python"
    def getlang(self):
        print(f"The language is {self.lang}")
    def showDetails(self):
        print("This is an Programmer")

E = Employee()
E.showDetails()
P = Programmer()
P.showDetails()
