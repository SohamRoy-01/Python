# problem 1

# f =open('poem.txt')
# t = f.read()
# if 'twinkle' in t:
#     print("twinkle is present")
# else:
#     print("twinkle is not there")
# f.close() 

# Problem 2

# def game():
#     return 484

# score=game()
# with open("hiscore0.txt") as f:
#     hiscore01 = (f.read())
# if hiscore01 =='':
#     with open("hiscore0.txt",'w') as f:
#         f.write(str(score))
# elif int(hiscore01)<score:
#     with open("hiscore0.txt",'w') as f:
#         f.write(str(score))


# Problem 3


# for i in range(2,21):
#     with open(f"tables1/Multiplication_tables_of_{i}.txt",'w') as f:
#         for j in range(1,11):
#             f.write(f"{i}X{j}={i*j}")
#             if j!=10:
#                 f.write("\n")

# Problem 4

# with open("sample1.txt") as f:
#     content = f.read()
# content = content.replace("donkey","$%^$$^#")

# with open("sample1.txt","w") as f:
#     f.write(content)
 
# problem 5
# words = ["donkey","name","the"]
# with open("sample1.txt") as f:
#     content = f.read()
#     for word in words:
#         content = content.replace(word,"$%^$$^#")
#     with open("sample1.txt","w") as f:
#         f.write(content)


# problem 6

# with open("log1.txt")as f:
#     a = f.read()

# if 'Python' in a.lower:
#     print("yes python is present")
# else:
#     print("No python is not prsent")

# Problem 7

# from email import contentmanager
# from re import I


# a =True
# i=1
# with open("log1.txt")as f:
    
#     while a:
#         a = f.readline()
#         if 'python' in a.lower():
#             print(a)
#             print(f"yes python is present on line number {i}")
#         i=i+1

                 
# problem 8

# with open("this1.txt") as f:
#     content = f.read()

# with open ("copy1.txt","w") as f:
#     f.write(content)

# problem 9

# file1 ="copy1.txt"
# file2 ="this1.txt"

# with open(file1) as f:
#     f1 =f.read()

# with open(file2) as f:
#     f2 =f.read()

# if f1==f2:
#     print("files are identical")
# else:
#     print("files are not identical")

# problem 10

# filename = "sample1.txt"
# with open(filename,"w") as f:
#     f.write("")

#  problem 11
import os

old_name = "sample1.txt"
new_name = "renamed_by_python.txt"

# renaming the file
os.rename(old_name,new_name)


#  problem 11 Alternative
# import os

# old_name = "sample3.txt"
# new_name ="renamed_by_python.txt"
# with open(old_name) as f:
#     content = f.read()
# with open(new_name,"w") as f:
#     f.write(content)

# # renaming the file
# os.remove(old_name)