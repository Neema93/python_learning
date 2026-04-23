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
# Loop Through a List
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
# Loop Through the Index Numbers
for i in range(len(thislist)):
  print(i)
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]
# Using a While Loop
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

""" List Methods
Python has a set of built-in methods that you can use on lists.

Method	Description
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list
"""