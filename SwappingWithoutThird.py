num1=int(input("Enter num1 : "))
num2=int(input("Enter num2 : "))

if num1<num2:
    print("Before Swapping : ",num1,num2)

    num2=num2+num1
    num1=num2-num1
    num2=num2-num1

    print("After Swapping : ",num1,num2)
else:
    print("Before Swapping : ",num1,num2)

    num1=num1+num2
    num2=num1-num2
    num1=num1-num2

    print("After Swapping : ",num1,num2)
