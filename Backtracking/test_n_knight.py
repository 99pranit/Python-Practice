def n_knight(n, target):
    a = [[False for _ in range(n)] for _ in range(n)]
    place_knights(a, 0, 0, target)

def place_knights(a, r, c, target):
    if target == 0:
        print_board(a)
        print(end='\n')
        return
    
    # If we have reached beyond the last row, return
    if r >= len(a):
        return

    # Move to the next row if the column exceeds the board size
    if c >= len(a[0]):
        place_knights(a, r + 1, 0, target)
        return
    
    # Try placing a knight at current position if it's safe
    if is_safe(a, r, c):
        a[r][c] = True
        place_knights(a, r, c + 1, target - 1)  # Recur with one less knight to place
        a[r][c] = False  # Backtrack

    # Try without placing a knight at the current position
    place_knights(a, r, c + 1, target)

def is_safe(a, r, c):
    # Check all possible moves of a knight
    if isValid(a, r - 2, c - 1) and a[r - 2][c - 1]:
        return False
    if isValid(a, r - 2, c + 1) and a[r - 2][c + 1]:
        return False
    if isValid(a, r - 1, c - 2) and a[r - 1][c - 2]:
        return False
    if isValid(a, r - 1, c + 2) and a[r - 1][c + 2]:
        return False
    return True

def isValid(a, r, c):
    # Ensure the position is within the board boundaries
    return 0 <= r < len(a) and 0 <= c < len(a[0])

def print_board(a):
    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j]:
                print('K', end=' ')
            else:
                print('X', end=' ')
        print()

n_knight(3 , 5)
