def primeOrNot(num):
    for i in range(2,num):
        if num%i==0:
            print("Not a prime number")
            break
    else:
        print("Prime number")

num=int(input("Enter a number : "))
if num>0:
    primeOrNot(num)
else:
    print("Enter a valid number")
