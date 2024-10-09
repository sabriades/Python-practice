#weight converter

weight_str=input("Weight: ")
weight=int(weight_str)
digit=input("(K)g or (L)bs: ")
if digit in ("K","k"):
    print("Your weight in Kg is: "+weight_str)
    conv=weight*2.205
    conv_str=str(conv)
    print("Your weight in Lbs is: "+conv_str)
elif digit in ("L","l"):
    print("Your weight in Lbs is: "+weight_str)
    conv=weight/2.205
    conv_str = str(conv)
    print("Your weight in Kg is :"+conv_str)
else:
    print("Invalid input. Digit K or L")

    digit1=input("(K)g or (L)bs: ")
    if digit1 in ("K","k"):
        print("Your weight in Kg is: " + weight_str)
        conv = weight * 2.205
        conv_str = str(conv)
        print("Your weight in Lbs is: " + conv_str)
    elif digit1 in ("L","l"):
        print("Your weight in Lbs is: " + weight_str)
        conv = weight / 2.205
        conv_str = str(conv)
        print("Your weight in Kg is :" + conv_str)
    else:
        print("Invalid input. Digit K or L")


