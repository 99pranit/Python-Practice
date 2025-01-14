def is_happy(value):
    slow = digit_sum(value)
    fast = digit_sum(digit_sum(value))
    while slow!=fast:
        if slow == 1 or fast == 1:
            return True
        slow = digit_sum(slow)
        fast = digit_sum(digit_sum(fast))
    return False

def digit_sum(value):
    sum = 0
    while value:
        rem = value%10
        sum = rem * rem + sum
        value = value//10
    return sum 


print(is_happy(19))