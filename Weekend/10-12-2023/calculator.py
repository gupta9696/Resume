msg='''Choice Operation :
1 - Addition
2 - Substraction
3 - Multiplication
4 - Division
5 - Percentage
6 - Discount
7 - Simple Interest
'''
msg1="Eneter First Value"
msg2="Eneter second Value"

choice=int(input(msg))

if(choice == 1):
    v1=int(input(msg1))
    v2=int(input(msg2))
    print("Addition :",v1+v2)
elif(choice == 2):
    v1=int(input(msg1))
    v2=int(input(msg2))
    print("Sub : ",v1-v2)
elif(choice == 3):
    v1=int(input(msg1))
    v2=int(input(msg2))
    print("Mul :",v1*v2)
elif(choice == 4):
    v1=int(input(msg1))
    v2=int(input(msg2))
    print("Div :",v1/v2)
elif(choice == 5):
       v1=int(input("Enter Base Value "))
       v2=int(input("Eneter Discount Percentage"))   
       dis=(v1 * v2) / 100
       print(" Discount Value :",dis)
       fc = int(input("You want price after discount 1 - > Yes    2 - > No"))
       if(fc == 1):print(v1 - dis)
       else: print("Thank you!")
       
elif(choice == 6):
       v1=int(input("Enter Base Value "))
       v2=int(input("Eneter Price Percentage reuired"))   
       dis=(v1 * v2) / 100
       print("After discount price :",v1 - dis)
       
elif(choice ==7):
    p1=int(input("Enter principle Value"))
    t1=int(input("Enter time in year"))
    r1=int(input("Enter Rate of interest"))
    si=(p1 * t1 * r1) / 100
    print("interest :", si)
    