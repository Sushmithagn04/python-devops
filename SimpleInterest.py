def simpleInterest(principle,rate,time):
    result=(principle*rate*time)/100
    return result

principle=int(input("Enter the principle amount : "))
rate=int(input("Enter the rate : "))
time=int(input("Enter the time : "))

print("Simple Interest : ", simpleInterest(principle,rate,time))
