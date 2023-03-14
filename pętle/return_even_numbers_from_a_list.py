# write a program that returns list of even numbers
# input: [6, 3, 5, 8, 4]
# expected output [6, 8, 4]


def get_even_numbers(nbs):
    empty_list = []
    for n in nbs:
        if n % 2 == 0:
            empty_list.append(n)
    return empty_list

