#  write a program that checks whether a given number is prime or not
#  input: 11
#  expected output: Prime

def get_prime_number(nb: int):
    if nb // nb == 1 and nb // 1 == nb and nb > 0:
        return "Prime"
    else:
        return "Not prime"