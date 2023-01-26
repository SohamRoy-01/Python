# Use open function to read the content of a file

# f = open('sample1.txt','r')  
f = open('sample1.txt') # by default it has 'r' mode
data =f.read(4)
print(data)
f.close() 