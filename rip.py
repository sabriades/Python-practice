print("I'm revising my Python skills. It's been a minute since I used Python")
age=20 #state a variable
print(age) #prints the value of the variable
my_sister="Pesca"
#declare a variable
is_at_home=False #False is boolean False value

name=input("what's your name? ") #requires a input
#function input returnes the value that we entered in the terminal window
#let's store this value: name
print("Hello "+name+"!") #string concatenation
birth_year=input("pls insert your birth year ")
#string convertion to int:
birth_year=int(birth_year)
age=2025-birth_year
age=str(age)
print("your age is "+age)
#if we have a float, we use float()
#function to convert the type of the variable
#int()
#float()
#bool()
#str()

example="string in upper method"
example=print(example.upper())
example_u="STRING IN LOWER METHOD"
example_u=print(example_u.lower())

dec="i have flz for you"
print(dec.replace("for","4"))
print(dec.find("for")) #index for the keyword given ("for")
print("for" in dec) #returns a boolean value - True or False
#24.00