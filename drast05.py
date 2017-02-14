# -*- coding: utf-8 -*-
from stack import *
st = createStack()
syn = True
while syn:
    ar = input (" Δώσε αριθμό ")
    if ar >0:
        push(st, ar)
    if ar ==0:
        syn = False
    if ar <0:
        ep = ar *-1
        for i in range(ep):
            if isEmpty(st):
                syn = False
                print "TELOS"
            else:
                it = pop(st)
                print "Αφαιρέθηκε το στοιχείο",it


