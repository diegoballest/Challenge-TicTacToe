import copy

'''
this method receives a string
and formats it if its a valid board.

filter method is for removing whitespaces in array
'''
WIDTH = 7
HEIGHT = 6
DEPTH = 5
VALUE = 10000000

def parse_string_to_game_format(string):
    board = ''
    boardArr = string.split(' ')
    boardArr = list(filter(None, boardArr))
    if (len(boardArr)!= 42):
        board = 'not a computable board'
        return board, boardArr
    for i, l, in enumerate(boardArr):
        if l == 'e':
          l = ' '
        board += str(l)
        if(i+1) %WIDTH != 0:
          board += ' |'
        if (i+1) %WIDTH == 0:
          board += '\n'
    return board, boardArr

# get the board current state and the player X or O
def win(b, p):
    # look for 4 horizontally
    for i in range(HEIGHT):
        for j in range(WIDTH - 3):
            if(b[i*WIDTH + j] == p and b[i*WIDTH + j+1] == p and b[i*WIDTH + j+2] == p and b[i*WIDTH + j+3] == p):
                return True
    # look for 4 vertically
    for i in range(HEIGHT - 3):
        for j in range(WIDTH):
            if(b[i*WIDTH + j] == p and b[(i+1)*WIDTH + j] == p and b[(i+2)*WIDTH + j] == p and b[(i+3)*WIDTH + j] == p):
                return True
    # look for 4 diagonally (from left to right)
    for i in range(HEIGHT - 3):
        for j in range(WIDTH - 3):
            if(b[i*WIDTH + j] == p and b[(i+1)*WIDTH + j+1] == p and b[(i+2)*WIDTH + j+2] == p and b[(i+3)*WIDTH + j+3] == p):
                return True
    # look for 4 diagonally (from right to left)
    for i in range(HEIGHT - 3):
        for j in range(3, WIDTH):
            if(b[i*WIDTH + j] == p and b[(i+1)*WIDTH + j-1] == p and b[(i+2)*WIDTH + j-2] == p and b[(i+3)*WIDTH + j-3] == p):
                return True
    return False

# should return only the empty spaces where it is valid to play
def getEmptySpaces(board):
    emptySpaces = []
    for i in range(HEIGHT):
        for j in range(WIDTH):
            if((board[i*WIDTH + j] == 'e' and i+1 < HEIGHT and board[(i+1)*WIDTH + j] != 'e') or (board[i*WIDTH + j] == 'e' and i+1 == HEIGHT)):
                emptySpaces.append(i * WIDTH + j)
    return emptySpaces

# alpha -> Maximizer; beta -> Minimizer
def minimax(boardArr, player, ai, human, alpha, beta, depth):
    al = alpha
    be = beta
    moves = [] # Hash array that looks like this -> [{'i': 1, 'score': 10}, {'i': 2, 'score': -10}]
    emptySpaces = getEmptySpaces(boardArr)
    best = -VALUE if player == ai else VALUE
    if(depth == DEPTH):
        # in here you could calculate the score by evaluating the board according to any heusristic
        # like the number of 'o's and 'x' or if there are two, or three of them together, etc.
        # By leaving the score in 0, it just finds finds and tries to stop losing positions, in the given depth
        return {'i' : -1, 'score' : 0}

    if(not emptySpaces):
        return {'i' : -1, 'score' : 0}

    for i in emptySpaces:
        temp = copy.deepcopy(boardArr)
        temp[i] = player
        next_move = {}
        next_move['i'] = i
        tempString = ' '.join(temp)
        tempBoard, tempBoardArr = parse_string_to_game_format(tempString)
        if(win(temp, ai)):
            next_move['score'] = 10
            return next_move
        elif(win(temp, human)):
            next_move['score'] = -10
            return next_move
        else:
            if(player == ai):
                res = minimax(tempBoardArr, human, ai, human, al, be, depth+1)
                best = max(best, res['score'])
                next_move['score'] = res['score']
                al = max(al, best)
            else:
                res = minimax(tempBoardArr, ai, ai, human, al, be, depth+1)
                best = min(best, res['score'])
                next_move['score'] = res['score']
                be = min(be, best)

        moves.append(next_move)
        if be <= al:
            break

		
    best = {}
    if(player == ai):
      maxScore = -VALUE
      for move in moves:
        if(move['score'] > maxScore):
          best = move
          maxScore = move['score']
    else:
      minScore = VALUE
      for move in moves:
        if(move['score'] < minScore):
          best = move
          minScore = move['score']
    return best

def valid_move(board, j):
    for row in range(HEIGHT-1):
        if(board[(row + 1)*WIDTH + j-1] != 'e'):
            return row*WIDTH + j-1
    return (HEIGHT-1)*WIDTH + j-1

def endGame(board):
	emptySpaces = getEmptySpaces(board)
	if(not emptySpaces):
		return "TIE"

	if(win(board, 'x')):
		return "WINNER: X"
	elif(win(board, 'o')):
		return "WINNER: O"

	return -1

def main():
    ai = 'x'
    human = 'o'

    # if ai is first
    boardStr = 'e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e x e e e'
    # boardStr = 'e e e e e e e e e e e e e e e e e e e e e e e e e x o x e x e x o x o e o x o o x o'
    turn = human

    board, boardArr = parse_string_to_game_format(boardStr)
    winner = endGame(boardArr)
    while(winner == -1):
        board, boardArr = parse_string_to_game_format(boardStr)
        print("1 |2 |3 |4 |5 |6 |7")
        print(board)
        if(turn == human):
          nextMove = int(input("\nType number >>"))
          boardArr[valid_move(boardArr, nextMove)] = turn
          turn = ai
        else:
          nextMove = minimax(boardArr, ai, ai, human, -VALUE, VALUE, 0)
          nextMove = nextMove['i']
          boardArr[nextMove] = turn
          turn = human

        boardStr = ' '.join(boardArr)
        winner = endGame(boardArr)


    board, boardArr = parse_string_to_game_format(boardStr)
    print(board,"\n", winner)




if __name__ == "__main__":
    # execute only if run as a script
    main()
