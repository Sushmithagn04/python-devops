def strLength(my_str):
    len_count=0
    for i in my_str:
        len_count=len_count+1
    return len_count

my_str="Hey, there!"

srtLen=strLength(my_str)
print("The length of the given string : ", srtLen)
