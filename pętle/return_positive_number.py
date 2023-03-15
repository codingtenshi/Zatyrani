#  write a program that checks whether a number in a list is positive,
#  negative or zero
# input: [5, 6, 8, 0, -4, -3]
# expected output: Positive


lst = [5, 6, 8, 0, -4, -3]
result = []


def get_positive_number(nbs):
    for n in nbs:
        if n > 0:
            result.append(n)
    return result


print(get_positive_number([5, 6, 8, 0, -4, -3]))