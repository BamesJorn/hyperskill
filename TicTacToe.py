N = 3
GRID_SIZE = N
rows, columns, diagonals = [], [], []

def main():
    field = ' ' * N * N
    field = [field[i] for i in range(len(field))]

    # create empty lists for rows, columns and diagonals
    global rows, columns, diagonals
    rows = [field[i*N:(i+1)*N] for i in range(N)]
    columns = [''.join(rows[i][j] for i in range(N)) for j in range(N)]
    diagonals = [''.join(rows[i][j] for i in range(N) for j in range(N) if i==j), \
                 ''.join(rows[i][j] for i in range(N) for j in range(N) if i+j == N-1)]
    # print empty field
    print_field()
    # first move is X
    X_move = True

    while True:
        x, y = make_move()              # prompt for coordinates of a new move
        update_field(x, y, X_move)
        X_move = not X_move             # swap from X to O and vice versa
        print_field()
        if match_ended():
            exit()


def print_field():
    global rows
    print('---' * N)
    for i in range(N):
        print('|', *rows[i], '|')
    print('---' * N)


def make_move():
    global rows
    while True:
        move = input("Enter the coordinates: ")
        if not move.replace(' ', '').isdigit():
            print("You should enter numbers!")
        else:
            x, y = (int(i) for i in move.split())
            if x < 1 or x > N or y < 1 or y > N:
                print(f'Coordinates should be from 1 to {N}!')
            elif rows[x-1][y-1] in 'XO':
                print("This cell is occupied! Choose another one!")
            else:
                break
    return x, y


def update_field(x, y, X_move):
    global rows, columns, diagonals
    rows[x-1][y-1] = 'X' if X_move else 'O'
    columns = [''.join(rows[i][j] for i in range(N)) for j in range(N)]
    diagonals = [''.join(rows[i][j] for i in range(N) for j in range(N) if i==j), \
                 ''.join(rows[i][j] for i in range(N) for j in range(N) if i+j == N-1)]


def match_ended():
    global rows, columns, diagonals
    field = []
    for i in range(N):
        field += rows[i]
    if "XXX" in (rows + columns + diagonals) or ['X'] * N in rows:
        print("X wins")
        return True
    elif "OOO" in (rows + columns + diagonals) or ['O'] * N in rows:
        print("O wins")
        return True
    elif ' ' not in field:
        print("Draw")
        return True
    else:
        return False


if __name__ == "__main__":
    main()