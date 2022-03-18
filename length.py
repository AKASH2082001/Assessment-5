def findLengthofstring(str):
    counter = 0
    for i in str:
        counter += 1
    return counter
str = input("enter the string:")
print(findLengthofstring(str))