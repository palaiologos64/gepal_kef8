ar=raw_input(" Δώσε λέξη ")
gr=["Q","W","E","R","T","Y","U","I","O","P","A","S","D","F","G","H","J","K","L","Z","X","C","V","B","N","M"]
c=0
for elem in ar:
    if elem in gr:
        c=c+1
print c
