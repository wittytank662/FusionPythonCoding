class Stack:
    def __init__(self):
        self.items = []
        
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)
    
    def isEmpty(self):
        return self.items ==[]
    
myStack = Stack()

print(myStack.isEmpty())

myStack.push("apples")
myStack.push("bananas")
myStack.push("cheese")
myStack.push("doughnuts")
myStack.push("eggs")

print(myStack.isEmpty())

print("The size of the stack is: " + str(myStack.size()))

print(myStack.pop())

print("After popping an element, the size of the stack is: " + str(myStack.size()))