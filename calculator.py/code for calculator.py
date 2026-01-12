

print("<<<<<<<<Calculator>>>>>>>>")


a=int(input("Number:"))
b=int(input("Number:"))

choice=input("Choose + or - or * or / or :")

if choice=="+":
    print(a+b)

elif choice=="-":
    print(a-b)

elif choice=="*":
    print(a*b)

elif choice=="/":
    if b != 0:
        print(a/b)
    else:
        print("Divison by zero not allowed")

        
else:
    print("Invalid Choice")