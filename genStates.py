# This project contains lexicographical algorithm soluution
# This is a algorithm related test

from itertools import permutations

def genStates():
    KeyLists = list(permutations("EEEEWWWW", 4))
    dict = {}
    dict = dict.fromkeys(KeyLists)

    KeyLists = list(dict.keys())
    for i in KeyLists:
        print("'{}'".format(''.join(i), end=""))

genStates()