import copy

'''
this method receives a string
and formats it if its a valid board.

filter method is for removing whitespaces in array
'''
WIDTH = 7
HEIGHT = 6

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

def getEmptySpaces(board):
    emptySpaces = []
    for i in range(len(board)):
        if(board[i] == 'e'):
            emptySpaces.append(i)
    return emptySpaces

def minimax(boardArr, player, ai, human):
    moves = [] # Hash array that looks like this -> [{'i': 1, 'score': 10}, {'i': 2, 'score': -10}]
    emptySpaces = getEmptySpaces(boardArr)

    if(not emptySpaces):
        return {'score' : 0}

    for i in emptySpaces:
        temp = copy.deepcopy(boardArr)
        temp[i] = player
        new_move = {}
        new_move['i'] = i
        tempString = ' '.join(temp)
        tempBoard, tempBoardArr = parse_string_to_game_format(tempString)

        if(win(temp, ai)):
            new_move['score'] = 10
            return new_move
        elif(win(temp, human)):
            new_move['score'] = -10
            return new_move
        else:
            if(player == ai):
                res = minimax(tempBoardArr, human, ai, human)
                new_move['score'] = res['score']
            else:
                res = minimax(tempBoardArr, ai, ai, human)
                new_move['score'] = res['score']

        moves.append(new_move)
		
    best = {}
    if(player == ai):
      maxScore = -10000000
      for move in moves:
        if(move['score'] > maxScore):
          best = move
          maxScore = move['score']
    else:
      minScore = 10000000
      for move in moves:
        if(move['score'] < minScore):
          best = move
          minScore = move['score']
    return best

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
    # boardStr = 'e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e e'
    boardStr = 'e e e e e e x e e e x e e x e e x e o e o e e e o e o x e x o x x x o e o x x o x o'
    turn = human

    board, boardArr = parse_string_to_game_format(boardStr)
    winner = endGame(boardArr)
    # while(winner == -1):
	   #  board, boardArr = parse_string_to_game_format(boardStr)
	   #  print(board)
	   #  if(turn == human):
	   #  	nextMove = int(input("\nType number >>"))
	   #  	boardArr[nextMove] = turn
	   #  	turn = ai
	   #  else:
	   #  	nextMove = minimax(boardArr, ai, ai, human)
	   #  	nextMove = nextMove['i']
	   #  	boardArr[nextMove] = turn
	   #  	turn = human

	   #  boardStr = ' '.join(boardArr)
	   #  winner = endGame(boardArr)


    # board, boardArr = parse_string_to_game_format(boardStr)
    print(board,"\n", winner)




if __name__ == "__main__":
    # execute only if run as a script
    main()
