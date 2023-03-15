#  write a program that gives list with a prime number
#  input: [11, 0, 2.3, -2, 2, 4]
#  expected output: [11, 2, 4]


def get_prime_number(nbs):
    empty_list = []
    for n in nbs:
        if n <= 1:
            continue
        if n // n == 1 and n // 1 == n:
            empty_list.append(n)
    return empty_list


