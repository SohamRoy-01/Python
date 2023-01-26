class Number:
    def __init__(self,num):
        self.num = num
    def __add__(self,num1):
        print("Lets add")
        return self.num + num1.num
    def __mul__(self,num1):
        print("Lets multiply")
        return self.num * num1.num
n1 = Number(8)
n2 = Number(6)
sum = n1 + n2 
mul1 = n1 * n2 
print(sum)
print(mul1)


