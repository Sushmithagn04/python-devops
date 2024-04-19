def collectNumbers(totalNumber):
    print("Enter the" ,totalNumber, "numbers")
    for i in range(0,totalNumber):
        element=float(input())
        myList.append(element)

def calculateAvg():
    total=0
    for i in range(0,len(myList)):
        total=total+myList[i]
    return (total/totalNumber)

myList=[]
totalNumber=int(input("Average of how many numbers? "))
collectNumbers(totalNumber)

avg=calculateAvg()
print("The Average is : ", avg)
