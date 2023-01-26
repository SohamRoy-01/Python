a = {1,3,4,5,1} # No repetition is allowed
a={} #This set create an empty dictionary and not an empty set
print(type(a))
print(a)

# An empty set which can be created using the below syntax :
b =set()
print(type(b))
# adding values to an set
b.add(4)
b.add(5)
b.add(6)
# b.add([6,5,8,9])  # cannot add list to a sets
b.add((9,2,3)) #can add tuple to a sets
# b.add({7:9}) #cannot add dict to a sets
print(b) 
# Operation Sets (Types)
print(len(b)) # prints the length of this set

b.remove(5)  # removes 5 from the set b Operation Set
print(b)
# b.intersection({5,6})
b.union({2,3})
# b.pop()
print(b)












