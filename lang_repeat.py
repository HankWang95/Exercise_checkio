def long_repeat(line):
    if line == "":
        return 0

    l = list(line)
    cl = []
    ci = 1
    for i in range(len(l)-1):
        if l[i] == l[i+1]:
            ci += 1
        else:
            cl.append(ci)
            ci = 1
    cl.append(ci)

    return sorted(cl)[-1]



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    print('"Run" is good. How is "Check"?')

