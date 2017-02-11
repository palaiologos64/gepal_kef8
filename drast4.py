def isSubstring(string,substring):
    if substring in string:
        apan = True
    else:
         apan = False
    return apan

def timeSubstring(string,substring):
    m =0
    lst=len(string)
    lsub =len(substring)
    for i in range (0,lst-lsub+1):
        t1=""
        for k in range(lsub):
            t1=t1+string[i+k]
        print t1
        if substring == t1:
            m = m+1
    return m

string ="kalimera"
substring ="li"
print isSubstring(string,substring)
print "***********************"
string ="kalimerarara"
substring ="ra"
print timeSubstring(string,substring)

