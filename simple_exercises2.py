#a few metods for strings:

dish='pesca grigliata'
#print(dish.upper()) #prints dish in UPPERCASE
#print(dish.replace('pesca','mela')) #replaces pesca with mela

#dish.metod --> function or metod is related to the object (strings)
print('pesca' in dish) #searches for pesca in dish, giving out true or false

##
#operators
# 10 // 3: double slashes gives us a whole number
# 10 % 3: modulus operator
# 10 ** 3: exponent operator (10 alla terza)
#example of code optimization
x=10
x=x+3 #increase value of 10 by 3
x+=3 #means the same, but less code

##
#comparison operators: >,>=,<,<=,==,!=

#logical operators
price=25
print(price>10 and price<30) #if both these conditions are true, then it prints "true"
print(price>10 or price<30) #if at least one of these conditions is true, it prints true
print(not price>30) #not operator inverts false to true and viceversa

#if statements - WIP
#age_in=input("age: ")
#age=int(age_in)

