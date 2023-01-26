# problem 1

# class Programmer:
#     company = "Microsoft"
#     def __init__(self,name,product):
#         self.name = name
#         self.product = product
#     def getDetails(self):
#         print(f"The name of the {self.company} Programmer is {self.name} in which he associated with the product is {self.product}")

# Soham = Programmer("Soham","skype")
# nohit = Programmer("Nohit","Github")
# Soham.getDetails()
# nohit.getDetails()

# problem 2

# class calculator:
#     def __init__(self,num):
#         self.number = num
#     def square(self):
#         print(f"The Square of given Number {self.number} is : {self.number**2}")
#     def squareRoot(self):
#         print(f"The Square of given Number {self.number} is : {self.number**0.5}")
#     def cube(self):
#         print(f"The Cube of given Number {self.number} is : {self.number**3}")


# user = int(input("Enter the number :\n"))
# a = calculator(user)
# a.square()
# a.squareRoot()
# a.cube()


# problem 3

# class Attribute:
#     a = "harry"
# object = Attribute()
# object.a = "vivek"
# # Attribute.a = "vivek" Its change the class attribute
# print(Attribute.a)
# print(object.a) #  Its doesn't change the class attribute it will generate an instance attribute

# problem 4

# class calculator:
#     def __init__(self,num):
#         self.number = num
#     def square(self):
#         print(f"The Square of given Number {self.number} is : {self.number**2}")
#     def squareRoot(self):
#         print(f"The Square of given Number {self.number} is : {self.number**0.5}")
#     def cube(self):
#         print(f"The Cube of given Number {self.number} is : {self.number**3}")
#     @staticmethod
#     def greet():
#         print("Hello!")
# user = int(input("Enter the number :\n"))
# a = calculator(user)
# a.greet()
# a.square()
# a.squareRoot()
# a.cube()

# problem 5

# class Train:          
#     def __init__(self,name,fare,seats):
#         self.name = name
#         self.fare = fare
#         self.seats = seats
#     def getStatus(self):
#         print("********")
#         print(f"The {self.name} train is here !")
#   
#       print(f"The seats available in the train are {self.seats}")
#         print("********")

#     def fareInfo(self):
#         print(f"The price of the ticket is {self.fare}")
#     def bookTickets(self):
#         if(self.seats>0):
#             print(f"Congrats! Your Ticket has been booked Your seat number {self.seats} is mailed for\nfurther details")
#             # self.seats -= 1
#             self.seats=self.seats-1
#         else:
#             print("Sorry! this train is fully booked")


# Intercity = Train("Rajdhani express: 14758",90,1000)
# Intercity.getStatus()
# Intercity.fareInfo()
# Intercity.bookTickets()
# Intercity.bookTickets()
# Intercity.getStatus()
        
# Problem 6
class Sample:
    def __init__(slf,name):
        slf.name = name        
obj = Sample("Harry")
print(obj.name)






