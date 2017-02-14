# -*- coding: utf-8 -*-
def createQuere():
    return []

def enqueque(queue,item):
    queue.append(item)

def isEmpty(queue):
    if len(queque)==0:
        apant = True
    else:
        apant =False
    return apant

def dequeque(queque):
    return queque.pop(0)

def arPelatwn(queque):
    apant = len(queque)
    return apant

def emfPelatwn(queque):
    for elem in queque:
        print elem
def epomPeletis(queque):
    ap = queque(0)
    return ap
def epilogi():
    print "1 Δημιουργία Ουράς"
    print "2 Προσθήκη Πελάτη "
    print "3  Αφαίρεση Πελάτη "
    print "4 Εμφάνιση τα ονόματα των πελατών"
    print "5 Αριθμός πελατών στην σειρά   "
    print "6 Εμφάνιση του επόμενου πελάτη"
    print "9  Τέλος"
    epil = input (" Δώσε επιλογή  ")
    return epil
def wait():
    a = raw_input (" Πατήσετε enter για συνέχεια")
syn = True
q=createQuere()
while syn:
    ep = epilogi()
    if ep == 1:
        q=createQuere()
    elif ep == 2:
        pel = raw_input ( "Δώσε Ονοματεπώνυμο Πελάτη")
        enqueque(q,pel)
    elif ep ==3:
        pel = dequeque(q)
        print "Αφαιρέθηκε από την ουρά ο Πελάτης ",pel
        wait()
    elif ep ==4:
        emfPelatwn(q)
        wait()
    elif ep == 5:
        arPelatwn(q)
        wait()
    elif ep ==6:
        epomPeletis(q)
        wait()
    elif ep == 9:
        syn = False
print " Τέλος"










