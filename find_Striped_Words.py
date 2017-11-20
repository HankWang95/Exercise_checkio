import re


def checkio(text):
    vowels = ('A', 'E', 'I', 'O', 'U', 'Y')
    c = 0
    for word in re.split(r'[,. ?]', text.upper()):
        if not re.search(r'\d', word):
            for i in range(len(word) - 1):
                if word[i] in vowels and word[i + 1] in vowels:
                    break
                if word[i] not in vowels and word[i + 1] not in vowels:
                    break
                if i == len(word) - 2 or i == len(word) - 1 or i == len(word):
                    c += 1
                    print(word)

    return c
