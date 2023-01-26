from turtle import up


my_Dict = {
    "Fast" : "In a Quick Moment",
    "Soham": "Hacking the Coding",
    "Marks": [1,2,3],
    "anotherdict" :{'Soham':'Coder'},
        1:5
}

# print(type(my_Dict.keys()))
# print(list(my_Dict.keys())) # Print the keys of Dictionary
# print(my_Dict.values())# print the values of the key
# print(my_Dict.items()) # all key and Values it display in the terminal
update_dict = {
    "keshab" : "Friend",
    "Orange" : "Fruits",
    "Boolean" :"True/False"
}

my_Dict.update(update_dict)# Update The values from the above
print(my_Dict)
my_Dict = my_Dict.get("Boolean") # Gives the value of the key :boolean
# my_Dict = my_Dict.get["Boolean"] # It throws an error for using list function
print(my_Dict)






