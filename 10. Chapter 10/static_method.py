class Employee:
    company = "Google"
    def getsalary(self,signature): # self is parameter which passes any object
        print(f"Salary for this employee working in {self.company} is {self.salary}\n{signature} ")
    @staticmethod
    def greet():
        print("Good morning, Sir!")
    @staticmethod
    def time():
        print("The title is 9am in the morning")
        
harry = Employee() 
harry.salary = 100000
harry.getsalary("Thanks")
harry.greet()
# Employee.getsalary(harry) When we recall self