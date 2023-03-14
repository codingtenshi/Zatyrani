#  write a program that checks whether a string is a palindrome or not
#  input; racecar
#  expected output: Palindrome

def is_palindrome(a):
    if a == a[:: -1]:
        return "Palindrome"
    else:
        return "Not palindrome"



