list = [1,2,3,4,5]
print(list)

print(list[3])
list[3] = 10
print(list)

tup = (1,2,3,4,5)
print(tup)
print(tup[3])
tup[3] = 10
print(tup)              #Error because tuple is immutable 

set = {1,2,3,4,5}
print(set)

dict = {
    "A" : 10,
    "B" : 20,
    "C" : 30
}

print(dict)
print(dict["C"])

dict2 = {
    "Name" : "Harsh",
    "Age"  : 18,
    "Roll no." : 24
}

print(dict2)
print(dict2["Name"])