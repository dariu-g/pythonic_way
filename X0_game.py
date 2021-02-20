import pprint

# X/0 game
theBoard = {'top-L':' ', 'top-M':' ', 'top-R':' ',
            'mid-L':' ', 'mid-M':' ', 'mid-R':' ',
            'bot-L':' ', 'bot-M':' ', 'bot-R':' '}

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-----')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-----')
    print(board['bot-L'] + '|' + board['bot-M'] + '|' + board['bot-R'])
    print('-----')

class Player:
    def __init__(self, name):
        self.name = name

    def modifyBoard(self, board, position, move):
        if position in positions:
            if board[position] != ' ':
                print('Position already occupied, choose another position:')
                new_position = input()
                board[new_position] = move
            else:
                board[position] = move
        else:
            print(f'Bad position input.\nThe positions names are: {positions}')
            print('Choose another position')
            new_position = input()
            board[new_position] = move

values = list(theBoard.values())

winning_positions = [['bot-L', 'bot-M', 'bot-R'], ['mid-L', 'mid-M', 'mid-R'],
                     ['top-L', 'top-M', 'top-R'], ['top-L', 'mid-L', 'bot-L'],
                     ['top-M', 'mid-M', 'bot-M'], ['top-R', 'mid-R', 'bot-R'],
                     ['top-L', 'mid-M', 'bot-R'], ['top-R', 'mid-M', 'bot-L']]

game_status = True
def game_over():
    for element in winning_positions:
        for pos in element:
            asdf = [theBoard[pos]]
            print(asdf)
        print('----')
    if len(values) == 9:
        print('Game over, you\'re equal')

print('Type Player1 name:')
p1 = Player(input())
print('Type Player2 name:')
p2 = Player(input())

positions = list(theBoard.keys())
print(f'Available position names are: {positions}')

while game_status:
    print(f'Choose your position {p1.name}(O):')
    position_p1 = input()
    p1.modifyBoard(theBoard, position_p1, 'O')
    printBoard(theBoard)
    game_over()
    print(f'Choose your position {p2.name}(X):')
    position_p2 = input()
    p2.modifyBoard(theBoard, position_p2, 'X')
    printBoard(theBoard)
    game_over()
