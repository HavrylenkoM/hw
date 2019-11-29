from math import sqrt


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    limit = sqrt(n)
    i = 2
    while i <= limit:
        if n % i == 0:
            return False
        i += 1
    return True

# НЕ СМОГ УДЕРЖАТЬСЯ И НЕ СВОРОВАТЬ КУСОК, ЧТО ВЫШЕ ИЗ ИНТЕРНЕТА


numbers = list(range(0, 100 + 1))

prost = list(map(is_prime, numbers))

prime_numbers = dict(zip(numbers, prost))

prnum = []

for key, value in prime_numbers.items():
    if value is True:
        prnum.append(key)


def kvadrat(num):
    return num * num


kvdrt = list(map(lambda x: x * x, prnum))


print(kvdrt)