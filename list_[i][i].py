def checkio(gr):
    gr_2 = []
    for i in gr:
        l = list(i)
        gr_2.append(l)

    if gr_2[0][0] == gr_2[1][1] == gr_2[2][2] or gr_2[0][2] == gr_2[1][1] == gr_2[2][0]:
        if gr_2[1][1] != '.':
            return gr_2[1][1]
    for i in range(3):
        if gr_2[i][0] == gr_2[i][1] == gr_2[i][2]:
            if gr_2[i][0] != '.':
                return gr_2[i][0]
        if gr_2[0][i] == gr_2[1][i] == gr_2[2][i]:
            if gr_2[0][i] != '.':
                return gr_2[2][i]

    return 'D'


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")


