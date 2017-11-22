def checkio(opacity):
    f_list = []
    o = 10000
    age_list = []
    age = 0

    def fib(n):
        return 1 if n <= 2 else fib(n - 1) + fib(n - 2)

    n = 0
    while 1:
        n += 1
        f = fib(n)
        if f > 10000:
            break
        else:
            f_list.append(f)
    print(f_list)
    while age<5000:
        if age in f_list or age == 0:
            o -= age
        else:
            o += 1
        age_list.append((o, age))
        age += 1
    print(age_list)
    for o, age in age_list:
        if o == opacity:
            return age
    return 0


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(10000) == 0, "Newborn"
    assert checkio(9999) == 1, "1 year"
    assert checkio(9997) == 2, "2 years"
    assert checkio(9994) == 3, "3 years"
    assert checkio(9995) == 4, "4 years"
    assert checkio(9990) == 5, "5 years"
