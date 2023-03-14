#  write a program that checks whether a number is positive,
#  negative or zero
# input: 5
# expected output: Positive


def get_positive_number(nb):
    if nb == 0:
        return False
    elif nb > 0:
        return True
    else:
        return False


result = get_positive_number(5)
print(result)
