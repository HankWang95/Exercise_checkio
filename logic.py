O_N = ("conjunction", "disjunction", "implication", "exclusive", "equivalence")

def boolean(x, y, o):
    if o == O_N[0]:
        return 1 if x == y == 1 else 0
    if o == O_N[1]:
        return 1 if x == 1 or y == 1 else 0
    if o == O_N[2]:
        return 0 if x == 1 and y == 0 else 1
    if o == O_N[3]:
        return 1 if x != y else 0
    if o == O_N[4]:
        return 1 if x == y else 0

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert boolean(1, 0, "conjunction") == 0, "and"
    assert boolean(1, 0, "disjunction") == 1, "or"
    assert boolean(1, 1, "implication") == 1, "material"
    assert boolean(0, 1, "exclusive") == 1, "xor"
    assert boolean(0, 1, "equivalence") == 0, "same?"

