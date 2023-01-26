# problem 1

# n = int(input("Enter the 1st number: "))
# n1 = int(input("Enter the 2nd number: "))
# n2 = int(input("Enter the 3rd number: "))

# def max(n,n1,n2):
#     if n>n1:
#        if n>n2:
#         return n
#        else: 
#         return n2
#     else:
#         if(n1>n2):
#             return(n1)
#         else:
#             return(n2)
# m = max(n,n1,n2)
# print("maximum value among these: ",str(m))

# problem 2

# c = float(input("Enter celcius degree (°C): "))
# def farenheit(c):
#     return((c * 9/5) + 32)
# f = farenheit(c)
# print(f"Farenheit temp is {str(f)}F")


# problem 4

# n = int(input("Enter the number: \n"))

# def natural_sum(n):
#     if n==1 or n==0:
#         return 1
#     else:
#         return (n*(n+1)/2)
# print(natural_sum(n))

# problem 5

# n = int(input("Enter the number: "))
# for i in range(n):
#     for j in range(i,n):
#         print("*",end='')
#     print()


# problem 6

# n = float(input("Enter the number in inches: "))
# p = ("Invalid Number please check it")
# d = (n*2.54)
# def inches(n):
#         if n<=0:
#             return p
#         else:
#             return d
# print(inches(n))

# problem 7

from xml.dom.minidom import CharacterData


a = ("   Soham is a python developer    ")
def remove_strip(string,word):
    b = string.replace(word,"")
    return b.strip()
c = remove_strip(a,"a")
print(c)

# problem 8

n = int(input("Enter the number: "))

def table(num):
    if n<=0:
        print("invalid number")
    else:
        for i in range (1,11):
            print(f"{num} x {i} = {num*i}")
table(n)

            




