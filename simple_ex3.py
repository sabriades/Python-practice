#if statements
temperature=25
if temperature>35:
    print("it's a hot day")
    print("drink plenty of water")
elif temperature>20: #elif=else if in python
        print("it's a nice day")

        ##
        #easy exercise: age check
age=input("age: ")
age_int=int(age)
print("your age is "+age)
if age_int>18:
    print("you're an adult!")
elif (age_int<18):
    print("you're still a baby!")
