# n = int(input("Enter the number: \n"))

# def factorial_iter(n):
#     product = 1
#     for i in range(n):
#         product = product * (i+1)
#     return(product)

# print(factorial_iter(n))


n = int(input("Enter the number: \n"))

def factorial_recursive(n):
    if n==1 or n==0:
        return 1
    else:
        return n * factorial_recursive(n-1)
print(factorial_recursive(n))

