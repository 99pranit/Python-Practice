def n_knight(n , target):
    a = [[False for _ in range(n)] for _ in range(n)]
    generate_safe(a , 0 , 0 , target)

def generate_safe(a , r , c , k):
    if k == 0:
        print_board(place(a))
        return
    if r >= len(a) or c >= len(a[0]):
        return
    for i in range(r, len(a)):
        for j in range(c if i == r else 0, len(a[0])):
            if(isSafe(a , i , j)):
                a[i][j] = True
                generate_safe(a , r + 1 , c , k - 1)
                a[i][j] = False

def isSafe(a , r , c):
    knight_moves = [
        (-2, -1), (-2, 1),
        (-1, -2), (-1, 2),
        (1, -2), (1, 2),
        (2, -1), (2, 1)
    ]
    for move in knight_moves:
        new_r, new_c = r + move[0], c + move[1]
        if inRange(a, new_r, new_c) and a[new_r][new_c]:
            return False
    return True

def inRange(a , r , c):
    return 0 <= r < len(a) and 0 <= c < len(a[0])


def place(a):
    board = []
    for r in range(len(a)):
        row = []
        for c in range(len(a[0])):
            row.append('K' if a[r][c] else 'X')
        board.append(row)
    return board


def print_board(board):
    for row in board:
        print(' '.join(row))
    print()

print(n_knight(4 , 4))