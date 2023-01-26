from binascii import a2b_base64
from cgitb import text
from tkinter import Variable
# problem 1

# a = int(input("Enter the 1st number: "))
# b = int(input("Enter the 2nd number: "))
# c = int(input("Enter the 3rd number: "))
# d = int(input("Enter the 4th number: "))

# # if (a>d):
# #     a1 = a
# else:
#     a1 = d

# if(b>c):
#     a2 = b
# else:
#     a2 = c

# if(a1>a2):
#     print(str(a1) + " is greatest")
# else:    
#     print(str(a2) + " is greatest")


# problem 2


# a = int(input("Enter the 1st Subjects: "))
# b = int(input("Enter the 2nd Subjects: "))
# c = int(input("Enter the 3rd Subjects: "))

# if(a<33 or b<33 or c<33):
#     print("You are fail bcz you have less than 33% in one of the subjects")

# elif(a+b+c)/3 <40:
#     print("You are fail due to total percentage less than 40")
# else:
#     print("Congratulations! You are passed")


# problem 3


# comment = input("Enter the text :\n")

# if ("Make a lot of money" in comment):
#     spam = True
# elif ("buy now" in comment):
#     spam = True
# elif ("Subscribe this" in comment):
#     spam = True
# elif ("click this" in comment):
#     spam = True
# else:
#     spam = False

# if(spam):
#     print("This text is spam")
# else:
#     print("this text is not spam")

# problem 4

# a = input("Enter your username :\n")

# if(len(a)<10):
#     print("Number of characters are less than 10")
# else:
#     print("Number of characters are not less or greater than 10")    

# Problem 5 

# Given_names =["soham","harry","keshab","anjali","arpan","souvik"]
# User = input("Enter the name :\n")
# if(User in Given_names):
#     print("Its a present in the list")
# else:
#     print("Its not present in the list")

# Problem 6

# Student_Marks = int(input("Input the marks :\n"))
# if(Student_Marks>=90 and Student_Marks<=100):
#     print("His grade is Excellent")
# elif(Student_Marks>=80 and Student_Marks<=90):
#     print("His grade is A")
# elif(Student_Marks>=70 and Student_Marks<=80):
#     print("His grade is B")
# elif(Student_Marks>=60 and Student_Marks<=70):
#     print("His grade is C")
# elif(Student_Marks>=50 and Student_Marks<=60):
#     print("His grade is D")
# elif(Student_Marks<50):
#     print("His grade is F(fail)")
# else:
#     print("Please enter valid number")


Given_post = str(input("enter the keywoard :\n"))
Text = Given_post.casefold()
if ("harry" in Text):
    print("yeah its talking about harry")
else:
    print("Its not talking about harry")









    




   





    



