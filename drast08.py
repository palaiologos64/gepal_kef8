# -*- coding: utf-8 -*-
def plVowel(lexis):
    fonienta = ['a','e','o','u','i','y']
    pl =0
    for xar in lexis:
        if xar in fonienta:
            pl = pl+1
    return pl
def moreVal (lista):
    mx =0
    for elem in lista:
        nvol = plVowel(elem)
        if nvol > mx:
            nvol = mx
            lexis = elem
    return lexis


print plVowel("kalimera")
l1 = ["test","Kalimera", "trast","ok","aaaaaaaaaaaaaaaaaaa"]
print moreVal(l1)