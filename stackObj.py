class stack:
    def __init__(self):
        self.stack =[]
        
    def isEmpty(self):
        l = len(self.stack)
        if l ==0:
            apan = True
        else:
            apan = False
            
        return apan    

    def push(self,item):
        self.stack.append(item)

    def pop(self):
         ap =-1
         l = len(self.stack)
         if l != 0:
             ap = self.stack.pop()
         return ap

  

st1= stack()
st1.push(10)
st1.push(15)
print st1.pop()
if st1.isEmpty():
    print "Αδεια η στοίβα"
else:
    print "**************"
print st1.pop()
if st1.isEmpty():
    print "Αδεια η στοίβα"
else:
    print "****"    
print st1.pop()
if st1.isEmpty():
    print "Αδεια η στοίβα"
else:
    print "****"      
#st1[0]=3


