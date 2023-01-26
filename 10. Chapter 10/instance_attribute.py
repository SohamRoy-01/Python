from pyclbr import Class


class Employee:  # Class Attribute
    company = "Google"
    salary = 100
    
soham = Employee()
rajni = Employee()
# soham.salary = 300  # Instance attribute (Atrribute prefers instance attribute over class attribute)
# rajni.salary = 400
soham.salary = 45
print(soham.salary)
print(rajni.salary)

# below line throws an error as address is not present in instance/class
# print(soham.address)