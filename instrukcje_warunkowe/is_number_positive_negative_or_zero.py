#  write a program that checks whether a number is positive,
#  negative or zero
# input: 5
# expected output: Positive


def get_positive_number(nb):
    if nb == 0:
        return "Zero"
    elif nb > 0:
        return "Positive"
    else:
        return "Negative"


result = get_positive_number(5)
print(result)
