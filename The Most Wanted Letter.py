def checkio(text):
    c = {}
    for i in list(text.lower()):
        if i in c:
            c[i] += 1
        else:
            c[i] = 1
    t = c.items()
    return (sorted(t, key=lambda x: (-x[1], x[0]))[0][0])

# 使用了string库
# import string
# def checkio(text):
# 
#     return max(string.ascii_lowercase,key = lambda x : text.lower().count(x))

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")