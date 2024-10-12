combination = []
def maze(a , c , r , p):
    if c == len(a[0]) -1 and r == len(a[0]) - 1:
        combination.append(p)
        return
    
    elif c == len(a[0])  or r == len(a[0]):
        return
    elif a[c][r] == 0:
        a[c][r] = 1
        if c == len(a[0]) - 1 and r == 0:
            maze(a , c - 1 , r , p + '1')
            maze(a , c , r + 1 , p + 'd')
        elif r == len(a[0]) - 1 and c == 0:
            maze(a , c , r - 1 ,  p + 'u')
            maze(a , c + 1 , r , p + 'r')
        elif r == 0 and c == 0:
            maze(a , c , r + 1 ,  p + 'd')
            maze(a , c + 1 , r , p + 'r')
        elif c == 0:
            maze(a , c  , r - 1 ,  p + 'u')
            maze(a , c + 1 , r ,  p + 'r')
            maze(a , c , r + 1 ,  p + 'd')
        elif r == 0:
            maze(a , c - 1 , r ,  p + 'l')
            maze(a , c + 1 , r ,  p + 'r')
            maze(a , c , r + 1 ,  p + 'd')
        else:
            maze(a , c  , r + 1 ,  p + 'd')
            maze(a , c  , r - 1 ,  p + 'u')
            maze(a , c + 1 , r ,  p + 'r')
            maze(a , c - 1 , r ,  p + 'l')
        a[c][r] = 0
    else:
        return

        


def path(n):
    n = 3
    a = [[0 for _ in range(n)] for _ in range(n)]
    maze(a , 0 , 0 , '')
    return a

path(3)
print(combination)