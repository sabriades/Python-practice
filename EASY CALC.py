first=input('input first number: ')
second=input('input second number: ')

operation=input('which operation: ')
if operation in ['+','-','*','/']:
    if operation=='+':
        print(round(float(first)+float(second),2))
    elif operation=='-':
        print(round(float(first)-float(second),2))
    elif operation=='*':
        print(round(float(first)*float(second),2))
    elif operation=='/':
        if float(second)==0:
            print('not valid')
        else:
            print(round(float(first)/float(second),2))

else:
    print('operator not valid')