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




