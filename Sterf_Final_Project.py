"""

Joe Sterf
 4/28/2019
 Python 1 - DAT-119 - Spring 2019
 Final Project
 Tic-Tac-Toe Game

"""

import random
#create dictionary build board and track player moves
board = {1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9'}

#create list to track which spaces have been played
spaces_taken = []

#prints tic-tac-toe board
def display_board():
    column_count = 0
    for location in board:
        column_count += 1
        if column_count < 3:
            print(board[location],'|', end = '\t')
        else:
            print(board[location])
            print('')
            column_count = 0

#check all possible combinations to see if player won
def check_winner(player, positions_selected):
    winner = 0

    if positions_selected[1] == player and positions_selected[2] == player and positions_selected[3] ==player:
        winner = 1
    elif positions_selected[4] == player and positions_selected[5] == player and positions_selected[6] == player:
        winner = 1
    elif positions_selected[7] == player and positions_selected[8] == player and positions_selected[9] == player:
        winner = 1
    elif positions_selected[1] == player and positions_selected[4] == player and positions_selected[7] == player:
        winner = 1
    elif positions_selected[2] == player and positions_selected[5] == player and positions_selected[8] == player:
        winner = 1
    elif positions_selected[3] == player and positions_selected[6] == player and positions_selected[9] == player:
        winner = 1
    elif positions_selected[1] == player and positions_selected[5] == player and positions_selected[9] == player:
        winner = 1
    elif positions_selected[3] == player and positions_selected[5] == player and positions_selected[7] == player:
        winner = 1
    else:
        winner = 0
    return winner

#records player's move
def player_move(player, position):
    #update board dictionary with player's move
    board[position] = player
    #add move to spaces taken list
    spaces_taken.append(int(position))

#resets board dictionary and spaces_taken list
def reset_game():
    #clear board if user wants to play again
    for location in board:
        board[location] = str(location)
    #clear spaces_taken list
    spaces_taken.clear()

#takes user input to determine which space they pick
def select_move(player_num):
    valid_move = 'no'
    #create input message based on player number
    display = 'Player ' + player_num + ' select a space for your move: '
    while valid_move == 'no':
        player_move = input(display)
        print()
        try:
            player_move = int(player_move)
        except:
            print('Error. Please select an open space.')
            print()
            valid_move = 'no'
        else:
            #make sure they didn't pick a space that was already taken
            if player_move in spaces_taken:
                print('Error. Please select an open space.')
                print()
                valid_move = 'no'
            #make sure player only selects 1 to 9
            elif player_move < 1 or player_move > 9:
                print('Error. Please select an open space.')
                print()
                valid_move = 'no'
            else:
                valid_move = 'yes'
    return player_move


#checks for win or draw
def game_status(one, two ):
    #If either player won or game is a draw show message
    keep_playing = 'y'
    did_1_win = check_winner(one, board)
    did_2_win = check_winner(two, board)
    total_moves = len(spaces_taken)
    if did_1_win == 0 and did_2_win == 0 and total_moves == 9:
        print('It\'s a draw.')
        keep_playing = 'n'
    elif did_1_win == 1:
        print('Player one wins!')
        keep_playing = 'n'
    elif did_2_win == 1:
        print('Player two wins!')
        keep_playing = 'n'
    return keep_playing

#picks a space for computer in one player mode
def computer_move():
    #randomly pick a position as long as it's not already taken
    move_taken = 'y'
    while move_taken == 'y':
        ai_move = random.randint(1,9)
        if ai_move in spaces_taken:
            move_taken ='y'
        else:
            print('The computer picked', ai_move)
            move_taken ='n'
    #once an open space is found return that value
    return ai_move

def main():
    continue_game = 'y'
    #show option for one or two player
    print('1. One player')
    print('2. Two player')
    valid_game = 'no'
    #check for valid reponse
    while valid_game == 'no':
        game_type = input('Select a game type: ')
        try:
            game_type = int(game_type)
        except:
            print('Invalid selection')
            valid_game = 'no'
        else:
            if game_type < 1 or game_type > 2:
                print('Invalid selection')
                valid_game = 'no'
            else:
                valid_game = 'yes'
    #one player game
    if game_type == 1:
        # have players select whether they are X or O
        print()
        valid_selection = 'no'
        while valid_selection != 'yes':
            player_1 = input('Player one, choose X or O: ')
            if player_1.lower() == 'x':
                player_1 = 'X'
                player_2 = 'O'
                print('The computer will be O.')
                print()
                valid_selection = 'yes'
            elif player_1.lower() == 'o':
                player_1 = 'O'
                player_2 = 'X'
                print('The computer will be X.')
                print()
                valid_selection = 'yes'
            else:
                print('That was not a valid choice.')
                valid_selection = 'no'
        # create initial game board
        display_board()
        # loop through game until someone wins
        while continue_game == 'y':
            # player 1 moves
            player_move(player_1, select_move('one'))
            # show updated board
            display_board()
            # see if anyone won or game ended in draw
            continue_game = game_status(player_1, player_2)
            # computer moves if game is still going on
            if continue_game != 'n':
                player_move(player_2, computer_move())
                display_board()
                continue_game = game_status(player_1, player_2)
    #two player game
    elif game_type == 2:
        #have players select whether they are X or O
        print()
        valid_selection = 'no'
        while valid_selection != 'yes':
            player_1 = input('Player one, choose X or O: ')
            if player_1.lower() == 'x':
                player_1 = 'X'
                player_2 = 'O'
                print('Player two, you will be O.')
                print()
                valid_selection = 'yes'
            elif player_1.lower() == 'o':
                player_1 = 'O'
                player_2 = 'X'
                print('Player two, you will be X.')
                print()
                valid_selection = 'yes'
            else:
                print('That was not a valid choice.')
                valid_selection = 'no'
        #create initial game board
        display_board()
        #loop through game until someone wins
        while continue_game == 'y':
            #player 1 moves
            player_move(player_1,select_move('one'))
            #show updated board
            display_board()
            #see if anyone won or game ended in draw
            continue_game = game_status(player_1,player_2)
            #player 2 moves if game is still going on
            if continue_game != 'n':
                player_move(player_2,select_move('two'))
                display_board()
                continue_game = game_status(player_1, player_2)
    #once game ends, see if user wants to play again
    play_again = input('Would you like to play again (y or n)? ').lower()
    #check for invalid responses
    while play_again != 'y' and play_again != 'n':
        print('Only y or n are valid responses.')
        play_again = input('Would you like to play again (y or n)? ').lower()

    #start game over if they select yes
    if play_again == 'y':
        reset_game()
        main()

if __name__ == "__main__":
    main()