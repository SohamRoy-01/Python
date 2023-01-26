class Employee:
    company = "Bharat Gas"
    salary = 5600
    salarybonus = 500
    # totalSalary = 6100

    @property # Getter method
    def totalSalary(self):
        return self.salary + self.salarybonus
    
    @totalSalary.setter # method
    def totalSalary(self,val):
        salarybonus = val - self.salary

e = Employee()
print(e.totalSalary)
e.totalSalary = 5800
print(e.salary)
print(e.salarybonus)

