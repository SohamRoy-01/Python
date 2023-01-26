class Emp:
    comp ="ITC"
    salary = 100
    location = "delhi"
    @classmethod  # Decorator
    def changeSalary(cls, sal):
        cls.salary=sal  # Create an instant variable
    # def changeSalary(self,sal):
    #     self.__class__.salary = sal
    
e = Emp()
print(e.salary)
e.changeSalary(458)
print(e.salary)
print(Emp.salary)

 