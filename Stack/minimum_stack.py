'''
Design a stack class that supports the push, pop, top, and getMin operations.

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
'''

class minimum_stack:
    def __init__(self):
        self.stack = []

    def pop(self):
        return self.stack.pop() if self.stack else None
    
    def push(self , val):
        self.stack.append(val)

    def top(self):
        return self.stack[-1]
    
    def get_min(self):
        mini = self.stack[0]
        l = len(self.stack) - 1

        while l:
            mini = min(mini , self.stack[l])
            l -= 1
        
        return mini
    

minStack = minimum_stack()
minStack.push(1)
minStack.push(2)
minStack.push(0)
print(minStack.get_min())
minStack.pop()
print(minStack.top())
print(minStack.get_min())