def strReverse(my_str):
    reverse_string=""
    for i in my_str:
        reverse_string= i + reverse_string
    return reverse_string
    
my_str=input("Enter a string : ")
str_rev=strReverse(my_str)
print("The reverse of the string is : ",str_rev)
