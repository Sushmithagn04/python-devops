def sumOfNNaturalNumbers(num):
    result=(num*(num+1)/2)
    return result

num=int(input("Enter a number: "))
if(num>0):
    sum=sumOfNNaturalNumbers(num)
    print("The Sum of N natural Numbers is: ",sum)
else:
    print("Enter a valid number!")
