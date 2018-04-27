import copy

'''
this method receives a string
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
        (board[2] == player and board[4] == player and board[6] == player)
    ):
        return True
    else:
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
    boardStr = 'e e e e x e e e e'
    turn = human

    board, boardArr = parse_string_to_game_format(boardStr)
    winner = endGame(boardArr)
    while(winner == -1):
	    board, boardArr = parse_string_to_game_format(boardStr)
	    print(board)
	    if(turn == human):
	    	nextMove = int(input("\nType number >>"))
	    	boardArr[nextMove] = turn
	    	turn = ai
	    else:
	    	nextMove = minimax(boardArr, ai, ai, human)
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
