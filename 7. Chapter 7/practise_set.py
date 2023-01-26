# problem 1

# a = int(input("Enter the given Number: "))
# for i in range (1,11) :
#     # print(str(a)+' x '+ str(i)+' = '+ str(a*i))
# # f strings
#     print(f"{a}X{i}={a*i}")

#  problem 2

# l1 = ["Harry","Soham","Sachin","Rahul"]
# for name in l1:
#     if name.startswith("S"):
#         print("Hello "+ name)

#  problem 3

# a = int(input("Enter the given Number: "))
# i = 1
# while i<11:
#     print(f"{a}X{i}={a*i}")
#     i =i+1

# problem 4

# a = int(input("Enter the given Number: "))
# pr = True
# if a>1: 
#     for i in range(2,a):
#         if a%i==0:
#             pr = False
#             break
#     if pr:
#         print("Its a prime number")
#     else:
#         print("Its not a prime number")

# problem 5


# n = int(input("Enter the number: "))
# print("sum of naturals numbers are",int((n*(n+1))/2))
 
# # Alternative 

# num = (int(input("Enter the number: ")))
# if num <0:
#     print("Enter a positive number")
# else:
#     sum = 0
#     while(num>0):
#         sum= sum+num
#         num = num-1
#     print("the sum of natural numbers: ",sum)

# problem 6

from re import X

# n! = 1 X 2 X 3 X 4 X 5 X.....X n

# n = int(input("Enter the number: "))
# factorial = 1
# if n<0:
#     print ("Please enter valid number")
# elif n == 0:
#     print("The factorial of 0 is 1")
# else:
#     for i in range(1,n+1):
#         factorial = factorial*i
#     print("The factorial of",n,"is",factorial)

# Decreasing Triangle star pattern


n = int(input("Enter the number of rows: "))
# outer loop to handle number of rows
for i in range(n):
    # inner loops to handle number of columns
    # values changing according to outer loop
    for j in range (i,n):
        # printing stars
        print('* ',end ="")
    print()
# problem 7

# n = int(input("Enter the number of rows: "))
# for i in range (n):
#     for j in range(i,n):
#         print(" ",end='')
#     for j in range(i):
#         print("*",end='')
#     for j in range(i+1):
#         print("*",end='')
#     print()

# problem 8

# n = int(input("Enter the number of rows: "))
# for i in range (n):
#     for j in range(i+1):
#         print("*",end='')
#     print()

# problem 9

# n = int(input("Enter the number of rows: "))
# for i in range (n):
#     for j in range (n):
#         if i==0 or i==n-1 or j==0 or j==n-1:
#             print("*",end='')
#         else:
#             print(" ",end='')
#     print()



# a = int(input("Enter the given Number: "))
# for i in reversed(range (1,11)):
#     # print(str(a)+' x '+ str(i)+' = '+ str(a*i))
# # f strings
#     print(f"{a}X{i}={a*i}")














    



