def simpleInterest(principal,rate,time):
    result=(principal*rate*time)/100
    return result

principal=float(input("Enter the principal amount : "))
rate=float(input("Enter the rate : "))
time=float(input("Enter the time : "))

print("Simple Interest : ", simpleInterest(principal,rate,time))
