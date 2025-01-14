def generate(s , c):
    if not s:
        print(c)
    else:
        for i in range(int(s[0]) , int(s[0]) + 3):
            c1 = c + chr(ord('a') + i)
            s1 = s[1:]
            generate(s1 , c1)
def phone_letter(n):
    generate(str(n) , '')
    
n = 91
phone_letter(n)   