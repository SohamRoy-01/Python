class Employee:
    company = "Google"
    def getsalary(self): # self is parameter which passes any object
        print(f"Salary for this employee working in {self.company} {self.salary}")

harry = Employee() 
harry.salary = 100000
harry.getsalary()
# Employee.getsalary(harry) When we recall self