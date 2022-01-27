from IPython.display import clear_output

def display_board(board):
    clear_output()
    print(board[7]+'|'+board[8]+'|'+board[9])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[1]+'|'+board[2]+'|'+board[3])
    print('')

def player_input():
    player1=''
    player2=''
    while player1!='X' and player1!='O':
        player1 = input("Please pick a marker 'X' or 'O'").upper()
    if player1=='X':
        player2='O'
    else:
        player2='X'
    return player1,player2

def place_marker(board, marker, position):
    board[position]=marker

def win_check(board, mark):
   
    win=[mark,mark,mark]
    
    if board[1:4]==win:
        print(mark+' WON!')
        return True
    elif board[4:7]==win:
        print(mark+' WON!')
        return True
    elif board[7:10]==win:
        print(mark+' WON!')
        return True
    elif board[1:10:4]==win:
        print(mark+' WON!')
        return True
    elif board[3:8:2]==win:
        print(mark+' WON!')
        return True
    elif board[1:8:3]==win:
        print(mark+' WON!')
        return True
    elif board[2:9:3]==win:
        print(mark+' WON!')
        return True
    elif board[3:10:3]==win:
        print(mark+' WON!')
        return True
    else:
        return False
    

    
import random

def choose_first():
    return str(random.randint(1,2))

def space_check(board, position):
    return board[position]==' '


def full_board_check(board):
    if True in [empty_field==' ' for empty_field in board]:
        return False
    else:
        return True    

def player_choice(board):
    position=0
    while position not in range(1,10):
        try:
            position = int(input('Please enter a number between 1-9: '))
            if position==0:
                continue
            try:
                if not space_check(board,position):
                    print('Field is not available! Try again!')
                    position=0
                    continue
            except:
                continue
                
        except:
            continue
        return position

def replay():
    print('Would you like to play again?')
    choice=''
    while choice not in ['Y','N']:
        choice=input('Enter Y or N :' ).upper()
    print(choice)
    if choice=='Y':
        return True
    else:
        return False

if __name__=='__main__':
    while True:
        print('Welcome to Tic Tac Toe!')
        board=['#',' ',' ',' ',' ',' ',' ',' ',' ',' ',]
        player1,player2=player_input()
        display_board(board)

        if choose_first()=='2':
            print('Player 2 goes first!')
            x=player1
            player1=player2
            player2=x
        else:
            print('Player 1 goes first!')


        while not full_board_check(board):
            print('Player {} turn'.format(player1))
            player_one_choice=player_choice(board)
            place_marker(board,player1,player_one_choice)
            display_board(board)
            if win_check(board,player1):
                break

            if full_board_check(board):
                print('Result is even!')
                continue

            print('Player {} turn'.format(player2))    
            player_two_choice=player_choice(board)
            place_marker(board,player2,player_two_choice)
            display_board(board)
            if win_check(board,player2):
                break


        if not replay():
            quit()
        else:
            continue