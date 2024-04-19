index=int(input("Enter the index for the series: "))
firstNum=0
secondNum=1
temp=0

print(firstNum)
print(secondNum)

for i in range(0,index):
    temp=firstNum+secondNum
    firstNum=secondNum
    secondNum=temp
    print(temp)

