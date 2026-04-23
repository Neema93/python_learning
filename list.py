thislist = ["apple", "banana", "cherry"]
print(thislist[1])
# change item
thislist[1] = "blackcurrant"
print(thislist)
# Change a Range of Item Values
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
# Insert Items
thislist.insert(2, "watermelon")
print(thislist)
# append value
thislist.append("orange")
print(thislist)
#extend list
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
# remove item
thislist.remove("mango")
print(thislist)
# Remove Specified Index
thislist.pop(1)
print(thislist)
del thislist[0]
print(thislist)
# Clear the List
thislist.clear()
print(thislist)