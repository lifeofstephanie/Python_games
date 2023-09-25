"""
display the game board with 9 position
make sure the board is empty
provide numbers for each cell so the players can refer to it
provide error error for placing on symbol in a filled cell
if player has 3 symbols in allign display you win message
"""
#create a blank board

board = [' ' for _ in range(9)]

# display the board


def printBoard():
    print("--------------")
    print("|",board[0],"|",board[1],"|",board[2],"|")
    print("--------------")
    print("|",board[3],"|",board[4],"|",board[5],"|")
    print("--------------")
    print("|",board[6],"|",board[7],"|",board[8],"|")
    print('--------------')
    


def check_win(player):

    #check rows

    for i in range(0,9,3):
        if board[0] == board[1] == board[2]==player:
            return True
        if board[3] == board[4] == board[5]==player:
            return True
        if board[6] == board[7] == board[8]==player:
            return True
        
        #check columns

    for i in range(3):
        if board[0] == board[3] == board[6]==player:
            return True
        if board[1] == board[4] == board[7]==player:
            return True
        if board[3] == board[5] == board[8]==player:
            return True
        
        #check diagonals

    if board[0] == board[4] == board[8]==player:
            return True
    if board[2] == board[4] == board[6]==player:
            return True
    return False

#check if the board is full

def check_board_full():
     return ' ' not in board

#main game loop

def play_game():
     current_player = 'X'
     game_over = False

     while not game_over:
          printBoard()

#get the players move

          position = int(input('Enter current position (1-9): '))-1

          #check if the position is valid

          if board[position] != ' ':
               print('Invalid Move. Try Again')
               continue
          
        #update the board with the players move

          board[position] = current_player

          #check if the current player has won

          if check_win(current_player):
               printBoard()
               print('Player', current_player, 'Wins!!')
               game_over = True
          elif check_board_full():
               printBoard()
               print('It is a tie')
               game_over = True
          else: 
               #switch to the other player

               current_player = 'O' if current_player =='X' else 'X'
# start the game
play_game()

        