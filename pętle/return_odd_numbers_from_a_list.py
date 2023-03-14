# write a program that returns list of odd numbers
# input: [6, 3, 5, 8, 4]
# expected output [3, 5]

def get_odd_numbers(nbs):
    empty_list = []
    for n in nbs:
        if n % 2 == 1:
            empty_list.append(n)
    return empty_list


