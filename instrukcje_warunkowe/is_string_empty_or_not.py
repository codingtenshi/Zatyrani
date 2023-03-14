#  write a program that checks whether a string is empty or not
# input: ''
# expected output: empty

def get_empty_string(string):
    if len(string) == 0:
        return ""
    else:
        return False


result = get_empty_string("")
print(result)
print(get_empty_string("jkaka"))