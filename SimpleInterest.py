def simpleInterest(principal,rate,time):
    result=(principal*rate*time)/100
    return result

principal=int(input("Enter the principal amount : "))
rate=int(input("Enter the rate : "))
time=int(input("Enter the time : "))

print("Simple Interest : ", simpleInterest(principal,rate,time))
