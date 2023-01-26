from ast import pattern


# Square pattern


# n= int(input("Enter the number of rows: "))
# for i in range(n):
#     for j in range (n): 
#         print('*',end=' ')
#     print()

# Increasing triangle pattern

# n = int(input("Enter the number of rows: "))
# # outer loop to handle number of rows
# for i in range(n):
#     # inner loops to handle number of columns
#     # values changing according to outer loop
#     for j in range (i+1):
#         # printing stars
#         print('* ',end ="")
#     print()

# Decreasing Triangle star pattern

# n = int(input("Enter the number of rows: "))
# # outer loop to handle number of rows
# for i in range(n):
#     # inner loops to handle number of columns
#     # values changing according to outer loop
#     for j in range (i,n):
#         # printing stars
#         print('* ',end ="")
#     print()
# Right side triangle

# n = int(input("Enter the number of rows: "))
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end='')
#     for j in range (0,i+1):
#         print('*',end ='')
#     print()


# n = int(input("Enter the number of rows: "))
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end ='')
#     for j in range(i,n):
#         print("*",end='')
# #     print()


# n = int(input("Enter the number of rows: "))
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end ='')
#     for j in range(i):
#         print("*",end='')
#     for j in range(i+1):
#         print("*",end='')
#     print()

# n = int(input("Enter the number of rows: "))
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end='')
#     for j in range(i,n-1):
#         print("*",end ='')
#     for j in range(i,n):
#         print("*",end ='')
#     print()

    
# n = int(input("Enter the number of rows: "))
# for i in range(n-1):
#     for j in range(i,n):
#         print(" ",end ='')
#     for j in range(i):
#         print("*",end='')
#     for j in range(i+1):
#         print("*",end='')
#     print()
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end='')
#     for j in range(i,n-1):
#         print("*",end ='')
#     for j in range(i,n):
#         print("*",end ='')
#     print()


n = int(input("Enter the number of rows: "))
for i in range(n-1):
    for j in range(i+1):
        print("*",end='')
    for j in range(i,n-1):
        print(" ",end='')
    for j in range(i,n-1):
        print(" ",end='')
    for j in range(i+1):
        print("*",end='')
    print()
for i in range(n):
    for j in range (i,n):
        print("*",end='')
    for j in range(i):
        print(" ",end='')
    for j in range(i):
        print(" ",end='')
    for j in range (i,n):
        print("*",end='')
    print()




   
