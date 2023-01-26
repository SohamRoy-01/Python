# problem 1

# from msvcrt import kbhit
# from re import I


# class C2dVec:
#     def __init__(self,i,j):
#         self.icap = i
#         self.jcap = j
#     def __str__(self) -> str:
#         return (f"The 2d vector is {self.icap}i + {self.jcap}j")    

        
# class C3dvec(C2dVec):
#     def __init__(self, i,j,k):
#         super().__init__(i, j)
#         self.kcap = k
#     def __str__(self) -> str:
#         return (f"The 3d vector is {self.icap}i + {self.jcap}j + {self.kcap}k")

# v2d = C2dVec(1,3)
# v3d = C3dvec(1,8,7)

# print(v2d)
# print(v3d)

#  Problem 2


# class Animals:
#     animalType = "Mammal"

# class Pets(Animals):
#     color = "white"
# class Dogs(Pets):
#     @staticmethod
#     def bark():
#         print("bhou bhou")

# d = Dogs()
# d.bark()

# Problem 3



class Employee:
    salary = 10000
    increment = 1.5
    
    @property
    def salaryAfterIncrement(self):
        return self.salary*self.increment

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self,sai):
        self.increment = sai/self.salary

e = Employee()
print(e.salaryAfterIncrement)
print(e.increment)
e.salaryAfterIncrement = 2000
print(e.increment)




