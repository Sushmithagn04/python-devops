def amount(principal,rate,time):
    Amount=principal * (pow((1+rate/100),time))
    CompdInterest=Amount-principal
    print("Compount Interest : ", CompdInterest)

principal=float(input("Enter the principal amount : "))
rate=float(input("Enter the rate : "))
time=float(input("Enter the time : "))

amount(principal,rate,time)
