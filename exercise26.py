# Second part of Tic Tac Toe game


# I have to create a list of lists to represent the board

#  then if the board has same character in a row, column or diagonal, the player wins


game_1 = [[1, 2, 0], [2, 1, 0],	[2, 1, 1]]
game_2 = [[2, 2, 0], [2, 1, 0],	[2, 1, 1]]
game_3 = [[1, 2, 0], [2, 1, 0],	[2, 1, 1]]
game_4 = [[0, 1, 0], [2, 1, 0],	[2, 1, 1]]
game_5 = [[1, 2, 0], [2, 1, 0],	[2, 1, 2]]
game_6 = [[1, 2, 0], [2, 1, 0],	[2, 1, 0]]
gameresult = [game_1, game_2, game_3, game_4, game_5, game_6]
def findWinner(_game):    
    for x in range(0, len(_game)):
        if(_game[x][0] == _game[x][1] == _game[x][2]):
            return _game[x][0]
        if(_game[0][x] == _game[1][x] == _game[2][x]):
            return _game[0][x]
    x = 0
    while x < len(_game) - 1:
        if _game[x][x] == _game[x+1][x+1]:
            if x == len(_game) - 2:
                return _game[x][x]    
            x += 1
        else:
            break    
    x = len(_game) - 1
    i = 0
    while x > 0:
        if _game[x][i] == _game[x-1][i+1]:
            if x == 1:
                return _game[x][i]
            x -= 1
            i += 1
        else:
            break    
    return 0
for game in gameresult:
    print("Winner on game " + str(game) + " is " + str(findWinner(game)))