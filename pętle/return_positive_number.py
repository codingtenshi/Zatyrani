#  write a program that checks whether a number in a list is positive
#  input [5, 6, 8, 0, -4, -3]
# expected output: [5, 6, 8]


lst = [5, 6, 8, 0, -4, -3]


def get_positive_number(nbs):
    result = []
    for n in nbs:
        if n > 0:
            result.append(n)
    return result





