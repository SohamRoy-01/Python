from pyclbr import Class


class Employee:  # Class Attribute
    company = "Google"

soham = Employee()
rajni = Employee()
soham.salary = 300  # Instance attribute
rajni.salary = 400

print(soham.company)
print(rajni.company)

print(soham.salary)
print(rajni.salary)
