#Check whether the string is palindrome or not.

s = str(input("Enter any string value: "))

def palindrome(s):
    return s == s[ : :-1]

s1 = palindrome(s)

if s1:
    print("Yes")
else:
    print("No!")