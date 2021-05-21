# homework

# Sa se scrie o functie care primeste un numar nedefinit de parmetrii si sa se calculeze
# suma parametrilor care reprezinta numere intregi sau reale
import math
import __some_sums__ as ss


def param_sum(*args, **kwargs):
    the_sum = 0
    for x in args:
        if type(x) is int or type(x) is float:
            the_sum += x
    return the_sum


print("Args: 1, 5, -3, 'abc', [12, 56, 'cad']")
print(f"Sum = {param_sum(1, 5, -3, 'abc', [12, 56, 'cad'])}\n")

print("No arguments")
print(f"Sum = {param_sum()}\n")

print("Args: 2, 4, ‘abc’, param_1=2")
print(f"Sum = {param_sum(2, 4, 'abc', param_1=2)}\n")


# Sa se scrie o functie care citeste de la tastatura si returneaza valoarea daca aceasta este un nr intreg
# altfel returneaza 0

def read_number():
    in_str = input("Enter number: ")
    if in_str.isnumeric():
        x = float(in_str)
        if x - math.floor(x) == 0:
            return math.floor(x)
    return 0


print(f"Input result: {read_number()}\n")

# 3 functii recursive pt sum:
print(f"Sum [0,n] = {ss.sum_0_to_n(10)}")
print(f"Sum even [0,n] = {ss.sum_even_0_to_n(10)}")
print(f"Sum odd [0, n] = {ss.sum_odd_0_to_n(5)}")


