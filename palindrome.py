def isPalindrome(s):
    return s == s[::-1]
s = input("enter the string:")
ans = isPalindrome(s)

if ans:
    print("the given string is palindrome")
else:
    print("the given string is not palindrome")