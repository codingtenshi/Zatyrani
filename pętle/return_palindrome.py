#  write a program that checks whether a string is a palindrome or not
#  input; racecar
#  expected output: Palindrome
palindrome = "racecar"
other = "son"


def get_palindrome(char):
    char_in_list = []

    for ch in char:
        char_in_list.insert(0, ch)
    reverted_char = ''.join(char[::-1])

    if char == reverted_char:
        return "Is palindrome"
    else:
        return "Is not palindrome"


# def get_palindrome(char):
#     if char == char[::-1]:
#         return "Is palindrome"
#     else:
#         return "Is not palindrome"


