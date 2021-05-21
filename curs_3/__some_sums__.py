def sum_0_to_n(n):
    if n == 0:
        return 0
    return n + sum_0_to_n(n - 1)


def sum_even_0_to_n(n):
    if n == 0:
        return 0
    if n % 2 != 0:
        return sum_even_0_to_n(n-1)
    return n + sum_even_0_to_n(n-1)


def sum_odd_0_to_n(n):
    if n == 0:
        return 0
    if n % 2 == 0:
        return sum_odd_0_to_n(n-1)
    return n + sum_odd_0_to_n(n-1)
