import copy

'''
this method receives an string
and formats it if its a valid board.

filter method is for removing whitespaces in array
'''
def parse_string_to_game_format(string):
    board = ''
    boardArr = string.split(' ')
    boardArr = list(filter(None, boardArr))
    if (len(boardArr)!= 9):
        board = 'not a computable board'
        return board
    for i, l, in enumerate(boardArr):
        if l == 'e':
            l = ' '
        board += str(l)
        if(i+1) %3 != 0:
            board += ' |'
        if (i+1) %3 == 0:
            board += '\n'

    return board, boardArr

#get the board current state and the player X or O
def win(board, player):
    if(
        (board[0] == player and board[1] == player and board[2] == player) or
        (board[3] == player and board[4] == player and board[5] == player) or
        (board[6] == player and board[7] == player and board[8] == player) or
        (board[0] == player and board[3] == player and board[6] == player) or
        (board[1] == player and board[4] == player and board[7] == player) or
        (board[2] == player and board[5] == player and board[8] == player) or
        (board[0] == player and board[4] == player and board[8] == player) or
        (board[3] == player and board[4] == player and board[6] == player)
    ):
        print("win")
        return True
    else:
        return False

def getEmptySpaces(board):
    emptySpaces = []
    for i in range(len(board)):
        if(board[i] == 'e'):
            emptySpaces.append(i)
    return emptySpaces


def main():
    board, boardArr = parse_string_to_game_format('e e e x o x o o e      ')

    emptySpaces = getEmptySpaces(boardArr)
    print(board)
    print(boardArr)
    print(emptySpaces)
    for i in emptySpaces:
        temp = copy.deepcopy(boardArr)
        temp[i] = 'x'
        print(temp)
        win(temp, 'x');



if __name__ == "__main__":
    # execute only if run as a script
    main()
