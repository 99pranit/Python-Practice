def sum_of_digit(n):
    if n == 0:
        return 0
    else:
        
        return n % 10 + sum_of_digit(int(n / 10))
    
print(sum_of_digit(1234))