def place(a):
    for r in range(0 , len(a) ):
        for c in range(0 , len(a[0])):
            if a[r][c]:
                a[r][c] = 'Q '
            else:
                a[r][c] = 'X '
    return a

def check(a , r):
    if r == len(a):
        a1 = place(a)
        for i in range (0 , len(a1)):
            print(a1[i])
        print(end='\n')
        
    else:
        for c in range (0 , len(a)):
            if is_safe(a , r , c):
                a[r][c]  = True
                check(a , r + 1)
                a[r][c] = False

def is_safe(a , r , c):
    # ignore vertical rowise
    for i in range(0 , r):
        if a[i][c]:
            return False
    # ignore left diagional
    min_left = min(r , c)
    for i in range(1 , min_left + 1):
        if a[r - i][c - i]:
            return False
    # ignore right diagonal
    min_right = min(r , len(a) - c - 1)
    for i in range(1 , min_right + 1):
        if a[r - i][c + i]:
            return False
    return True
        
def n_queen(n): 
    a = [[False for _ in range(n)] for _ in range(n)]
    check(a , 0 )



n_queen(4)