def createStack():
    return []
def push(stack,item):
    stack.append(item)
def pop(stack):
    return stack.pop()
def isEmpty(stack):
    if len(stack)==0:
        ap = True
    else:
        ap = False
    return ap

st = createStack()
lexis = raw_input (" Δώσε λέξη  ")
for elem in lexis:
    push(st,elem)
s=""    
while not isEmpty(st):
    s=s+ pop(st)
print s
