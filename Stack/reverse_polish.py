'''
You are given an array of strings tokens that represents a valid arithmetic expression in Reverse Polish Notation.
'''
def reverse_polish(tokens):
    stack = []
    for t in tokens:
        if t == '*':
            second , first = stack.pop() , stack.pop()
            stack.append(int(first) * int(second))
        elif t == '/':
            second , first = stack.pop() , stack.pop()
            stack.append(int(first) / int(second))
        elif t == '+':
            second , first = stack.pop() , stack.pop()
            stack.append(int(first) + int(second))
        elif t == '-':
            second , first = stack.pop() , stack.pop()
            stack.append(int(first) - int(second))
        else:
            stack.append(int(t))

    return stack.pop()


print(reverse_polish(["1","2","+","3","*","4","-"]))

