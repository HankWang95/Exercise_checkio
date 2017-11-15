def checkio(i):
    # replace this for solution
    import string
    s = set(i)
    a = set(string.ascii_lowercase)
    b = set(string.ascii_uppercase)
    c = set(string.digits)
    print(a & s and b & s and c & s)
    return  bool(a & s) and bool(b & s) and bool(c & s) and len(i) >= 10


# Some hints
# Just check all conditions


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")