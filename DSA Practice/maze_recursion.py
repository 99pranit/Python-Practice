combination = []
def maze(r , c , p):
    if c == 1 and r == 1:
        combination.append(p)
        return
    elif c == 1:
        maze(r - 1 , c , p + 'r')
    elif r == 1:
        maze(r , c - 1 , p + 'd')
    else:
        maze(r - 1 , c - 1 , p + 'dia')
        maze(r - 1 , c , p + 'r')
        maze(r , c - 1 , p + 'd')

maze(3 , 3 , '')
print(combination)