def hcf(num1 , num2):
    if(num1 == 0):
        return num2
    else:
        return hcf(num2 % num1 , num1)
    
def lcm(num1 , num2):
    h = hcf(num1 , num2)
    return ((num1 * num2) / h)
    
print(hcf(4,6))
print(lcm(4,6))