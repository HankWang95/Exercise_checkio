class Friends:
    def __init__(self, connections):
        friend_set = set()
        for x, y in connections:
            friend_set.add((x,y))
        self.friend_set = friend_set

    def add(self, connection):
        (x, y) = connection
        if (x,y) in self.friend_set:
            return False
        else:
            self.friend_set.add((x,y))
            return True

    def remove(self, connection):
        (x,y) = connection
        if (x,y) in self.friend_set:
            self.friend_set.remove((x,y))
            return True
        else:
            return False

    def names(self):
        self.name = set()
        for x, y in self.friend_set:
            self.name.add(x)
            self.name.add(y)
        return self.name


    def connected(self, name):
        self.con = set()

        for (x,y) in self.friend_set:
            if name == y:
                self.con.add(x)
            elif name == x:
                self.con.add(y)
            else:
                continue
        #print(self.con)
        return self.con





if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    letter_friends = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"}))
    digit_friends = Friends([{"1", "2"}, {"3", "1"}])
    assert letter_friends.add({"c", "d"}) is True, "Add"
    assert letter_friends.add({"c", "d"}) is False, "Add again"
    assert letter_friends.remove({"c", "d"}) is True, "Remove"
    assert digit_friends.remove({"c", "d"}) is False, "Remove non exists"
    assert letter_friends.names() == {"a", "b", "c"}, "Names"
    assert letter_friends.connected("d") == set(), "Non connected name"
    assert letter_friends.connected("a") == {"b", "c"}, "Connected name"

