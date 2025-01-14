def subset(s , c):
    combinations = []
    if not s:
        print(c)
        return 
    if s:
        ch = s[0]
        subset(s[1:] , c +ch)
        subset(s[1:] , c)

s = 'asd'
print(subset(s , ''))