import Stack
s = Stack.Stack()

def sortStack(og): # passes a stack as a parameter
    h = Stack.Stack()
    while not og.isEmpty():
        cur = og.pop()
        while not h.isEmpty() and int(cur) > int(h.peek()):
            og.push(h.pop())
        h.push(cur)
    while not h.isEmpty():
        og.push(h.pop())

s.push(3)
s.push(4)
s.push(7)
s.push(2)
s.push(1)
s.push(5)
s.printStack()

sortStack(s)
s.printStack()