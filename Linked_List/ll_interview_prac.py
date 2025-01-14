def cycle(self):
    first = self.head
    second = first.next

    while first:
        if first == second:
            print('Cycle Present')
            return
        first = first.next
        second = second.next.next 

    print('Cycle Not Present')

def is_happy(value):
    slow = digit_sum(value)
    fast = digit_sum(digit_sum(value))
    while slow!=fast:
        if slow == 1 or fast == 1:
            return True
        else:
            slow = digit_sum(slow)
            fast = digit_sum(digit_sum(fast))
    return False

def digit_sum(value):
    sum = 0
    while value:
        rem = value%10
        sum = value * value + sum
        value = value/10
    return sum 