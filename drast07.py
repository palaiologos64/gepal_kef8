# -*- coding: utf-8 -*-
def maxWord(lista):
    mx=0
    for elem in lista:
        if len(elem)> mx:
            mx = len(elem)
            lexis= elem
    return lexis
l1=["test","Python", "v12","yyccccxxx"]
print maxWord(l1)