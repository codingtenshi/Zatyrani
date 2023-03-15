#  write a program that checks whether a number in a list is negative
#  input [5, 6, 8, 0, -4, -3]
#   expected output: [-4, -3]

e = [5, 6, 8, 0, -4, -3]


def get_negative_number(e):
    empty = []
    for n in e:
        if n < 0:
            empty.append(n)
    return empty


