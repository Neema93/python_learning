#inside quote
print("Hello")


#singleline varible
a = "Hello"
print(a)


#mulitiline variable
b = """Hello
This is Neema.
My age is 32.
""" 
print(b)


# find length of string
x = "Hello, World!"
print(len(x))

#check string
txt = "The best things in life are free!"
print("free" in txt)

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

#check if not
txt = "The best things in life are free!"
print("expensive" not in txt)

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

#Slicing Strings
b = "Hello, World!"
print(b[2:5])
print(b[:5])
print(b[2:])