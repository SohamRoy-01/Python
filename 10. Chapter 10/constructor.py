class Employee:
    company = "Google"
    
    def __init__(self,name,salary,subunit):
        self.name = name
        self.salary = salary
        self.subunit = subunit
        print("Employee is created")
    def getDetails(self):
        print(f"the name of the employee is {self.name}")
        print(f"the salary of the employee is {self.salary}")
        print(f"the subunit of the employee is {self.subunit}")
    def getsalary(self): # self is parameter which passes any object
        print(f"Salary for this employee working in {self.company} is {self.salary}")
    @staticmethod
    def greet():
        print("Good morning, Sir!")

harry = Employee("Soham",100,"Youtube")
harry.getDetails()
harry.getsalary()
