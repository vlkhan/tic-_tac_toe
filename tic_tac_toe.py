board = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def draw_board():
    print('____________')
    print(f' {board[0]} | {board[1]} | {board[2]} |')
    print('____________')
    print(f' {board[3]} | {board[4]} | {board[5]} |')
    print('____________')
    print(f' {board[6]} | {board[7]} | {board[8]} |')
    print('____________')


def step_(move, current_player):
    if move > 9 or move < 1 or (board[move-1] in ('X', 'O')):
        return False
    else:
        board[move-1] = current_player
        return True


def check_win():
    win = False
    win_condition = (
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # горизонт
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # вертикаль
        [0, 4, 8], [2, 4, 6]  # диагональ
    )
    for i in win_condition:
        if board[i[0]] == board[i[1]] == board[i[2]]:
            win = board[i[0]]

    return win


def start():
    current_player = 'X'
    step = 1
    draw_board()
    while step < 10 and check_win() == False:
        move = int(input(
            f'Ходит игрок {current_player}. Выберите цифру, на которую хотите поставить свой символ: '))

        if (step_(move, current_player)):
            draw_board()
            if current_player == 'X':
                current_player = 'O'
            else:
                current_player = 'X'
        else:
            print('Неверный номер! Повторите')

        step += 1

    if step == 10 and check_win() == False:
        print('Ничья')
    else:
        print(f'Победил игрок - {check_win()}')


print('Добро пожаловать в игру "Крестики-нолики".')
print('Для игры используйте латинские заглавные "Х" и "О"')
start()
