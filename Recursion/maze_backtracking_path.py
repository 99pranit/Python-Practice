combination = []
def maze(a , c , r , p):
    if c == len(a[0]) -1  and r == len(a[0]) -1  :
        a[c][r] = p
        print(a )
        a[c][r] = 0
        return
    
    elif c == len(a[0]) or r == len(a[0]):
        return
    elif a[c][r] == 0:
        a[c][r] = p
        if r == 0 and c == 0:
            maze(a , c , r + 1 ,  p + 1)
            maze(a , c + 1 , r , p + 1)
        elif c == len(a[0]) - 1 and r == 0:
            maze(a , c - 1 , r , p + 1)
            maze(a , c , r + 1 , p + 1)
        elif r == len(a[0]) - 1 and c == 0:
            maze(a , c , r - 1 ,  p + 1)
            maze(a , c + 1 , r , p + 1)
        elif c == 0:
            maze(a , c  , r - 1 ,  p + 1)
            maze(a , c + 1 , r ,  p + 1)
            maze(a , c , r + 1 ,  p + 1)
        elif r == 0:
            maze(a , c - 1 , r ,  p + 1)
            maze(a , c + 1 , r ,  p + 1)
            maze(a , c , r + 1 ,  p + 1)
        else:
            maze(a , c  , r + 1 ,  p + 1)
            maze(a , c  , r - 1 ,  p + 1)
            maze(a , c + 1 , r ,  p + 1)
            maze(a , c - 1 , r ,  p + 1)
        a[c][r] = 0
    else:
        return

        


def path(n):
    n = 3
    a = [[0 for _ in range(n)] for _ in range(n)]
    maze(a , 0 , 0 , 0)
    return a

path(3)