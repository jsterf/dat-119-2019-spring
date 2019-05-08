"""

Joe Sterf
 5/8/2019
 Python 1 - DAT-119 - Spring 2019
 Final Project
 Tic-Tac-Toe Game

"""
import os
import random

# checks if top_ten files already exists. Variable will be True if the file is there, False if not
top_ten_exists = os.path.isfile('top_ten.txt')

#create dictionary build board and track player moves
board = {1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9'}

#constant that contains all the winning combinations
WINNING_COMBINATIONS = {1:[1,2,3],2:[4,5,6],3:[7,8,9],4:[1,4,7],5:[2,5,8],6:[3,6,9],7:[1,5,9],8:[3,5,7]}

#create empty dictionaries to store top ten high score
top_ten = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0}
temp_top_ten = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0}

#create list to track which spaces have been played
spaces_taken = []

#set up global variables to track games played and games won by each player
games_played = 0
player_one_wins = 0
player_two_wins = 0
winning_player = 0
computer_move_count = 0
player_1 = ''
player_2 = ''

#if user selects play again they can't change from one to two player
new_game = 0
game_selection = 0

#loads top_ten files to dictionary
def load_file():
    #if top_ten file exists open in readonly mode
    if top_ten_exists == True:
        top_ten_file = open('top_ten.txt', 'r')
        top_ten_item = top_ten_file.readline()
        list_value = 1
        #loop through file and add to todo_list list until you reach end of file
        while list_value < 11:
            top_ten_item = top_ten_item.rstrip('\n')
            if top_ten_item == '':
                top_ten[list_value] = 0
            else:
                top_ten[list_value] = top_ten_item
            list_value += 1
            top_ten_item = top_ten_file.readline()
        #close file when done writing to dictionary
        top_ten_file.close()

#save top tne list to file
def save_file():
    temp_top = open('top_ten_temp.txt', 'w')
    list_value = 1
    #write top ten_list to top_temp file
    while list_value < 11:
        temp_top.write(str(top_ten[list_value]) + '\n')
        list_value += 1
    #close temp file
    temp_top.close()
    #delete existing top ten files is they exist
    if  top_ten_exists == 'True':
        os.remove('top_ten.txt')
    #rename temp file
    os.rename('top_ten_temp.txt', 'top_ten.txt')

#checks for new high score and updates dictionary accordingly
def high_score():
    global player_one_wins
    place = 1
    #loop through top ten list.  Stop if user wants to save score
    while place < 11:
        
        if player_one_wins > int(top_ten[place]):
            print('New high score!')
            break
        
        place += 1
    
    #Copy top ten to temp dictionary and replace score with new top score and move all other scores done one
    i = 1
    position_minus_one = 1
    while i < 11:
        #replace with new top score
        if place < 10:
            if i == place:
                temp_top_ten[i] = player_one_wins
                #subtract one from position so next loop pushes scores down one. Example position 2 now becomes third highest score
                position_minus_one -= 1
            else:
                temp_top_ten[i] = top_ten[position_minus_one]
        #if replacing the 10th highest score loop through 1-9 then just replace 10     
        else:
            if i < 10:
                temp_top_ten[i] = top_ten[i]
            else:
                temp_top_ten[i] = player_one_wins
        
        
        
        i += 1
        position_minus_one += 1

    #Copy temp dictionary back to top ten dictionary
    c = 1
    while c < 11:
        if temp_top_ten[c] == '':
            top_ten[c] = 0
        else:
            top_ten[c] = temp_top_ten[c]
        c += 1

def display_score():
    print('High Scores:')
    i = 1
    while i < 11:
        print(i,':',top_ten[i])
        i += 1
    
    
    
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

#track how many games each player has won
def score(num_players, winner):
    global games_played
    global player_one_wins
    global player_two_wins
    global winning_player

    games_played += 1
    #if single player just show games won out of total games.
    if num_players == 1 or num_players == 2:
        if winner == 1:
            player_one_wins += 1
            print('You have won', player_one_wins,'out of',games_played,'games.')
        else:
            print('You have won', player_one_wins, 'out of', games_played, 'games.')
    #if two player then show total of each player
    elif num_players == 3:
        if winner == 1:
            player_one_wins += 1
            print('Player one has won',player_one_wins,'games.')
            print('Player two has won', player_two_wins,'games.')
        elif winner == 2:
            player_two_wins += 1
            print('Player one has won', player_one_wins, 'games.')
            print('Player two has won', player_two_wins, 'games.')
        else:
            print('Player one has won', player_one_wins, 'games.')
            print('Player two has won', player_two_wins, 'games.')

#determine if there is a winning move depending on the player you select
def smart_move(player, correct):
    #loop through winning combinations
    for combo in  WINNING_COMBINATIONS:
        positions = WINNING_COMBINATIONS[combo]
        i = 0
        num_correct = 0
        num_blank = 0
        blank_position = 0
        #loop through the board for the winning combinations and see if a player is there or it's blank
        while i <3:

            if board[positions[i]] == player:
                num_correct += 1
            elif board[positions[i]] != 'X' and board[positions[i]] != 'O':
                num_blank +=1
                blank_position = positions[i]
            i += 1
        #if player selected has two positions and one blank then break loop and make that the computer move
        if num_correct == correct and num_blank >= 1:
            break
        else:
            blank_position = 0
    return blank_position

#check all possible combinations to see if player won
def check_winner(player, positions_selected):
    winner = 0

    for combo in WINNING_COMBINATIONS:
        winning_combo = WINNING_COMBINATIONS[combo]
        if positions_selected[winning_combo[0]] == player and positions_selected[winning_combo[1]] == player and positions_selected[winning_combo[2]] == player:
            winner = 1
            #if a winning combination is found stop looping through options.
            #break function found online https://www.digitalocean.com/community/tutorials/how-to-use-break-continue-and-pass-statements-when-working-with-loops-in-python-3
            break
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
    global computer_move_count
    #clear board if user wants to play again
    for location in board:
        board[location] = str(location)
    #clear spaces_taken list
    spaces_taken.clear()
    #reset computer move count
    computer_move_count = 0

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
    global winning_player
    keep_playing = 'y'
    did_1_win = check_winner(one, board)
    did_2_win = check_winner(two, board)
    total_moves = len(spaces_taken)
    if did_1_win == 0 and did_2_win == 0 and total_moves == 9:
        print('It\'s a draw.')
        keep_playing = 'n'
        winning_player = 0
    elif did_1_win == 1:
        print('Player one wins!')
        keep_playing = 'n'
        winning_player = 1
    elif did_2_win == 1:
        print('Player two wins!')
        keep_playing = 'n'
        winning_player = 2
    return keep_playing

#picks a space for computer in one player mode
def computer_move(difficultly):
    global  computer_move_count
    global player_1
    global player_2
    #expert difficultly.  Computer plays to win or draw.
    if difficultly == 2:
        if computer_move_count == 0:
            #try for center first
            if 5 not in spaces_taken:
                ai_move = 5
            else:
            #randomly pick a position as long as it's not already taken
                move_taken = 'y'
                while move_taken == 'y':
                    ai_move = random.randint(1,9)
                    if ai_move in spaces_taken:
                        move_taken ='y'
                    else:

                        move_taken ='n'
        else:
            #see if computer can win
            if smart_move(player_2, 2) != 0:
                ai_move = smart_move(player_2, 2)

            #if computer can't win see if it can top player from winning
            elif smart_move(player_1, 2) != 0:
                ai_move = smart_move(player_1, 2)

            #if computer can't win or block pick a position next to existing selection
            elif smart_move(player_2, 1) != 0:
                ai_move = smart_move(player_2, 1)

            else:
            #randomly pick a position as long as it's not already taken
                move_taken = 'y'
                while move_taken == 'y':
                    ai_move = random.randint(1,9)
                    if ai_move in spaces_taken:
                        move_taken ='y'
                    else:

                        move_taken ='n'
    #easy difficultly.  Computer picks 5 first then just picks randomly
    else:
        if computer_move_count == 0:
            # try for center first
            if 5 not in spaces_taken:
                ai_move = 5
            else:
                # randomly pick a position as long as it's not already taken
                move_taken = 'y'
                while move_taken == 'y':
                    ai_move = random.randint(1, 9)
                    if ai_move in spaces_taken:
                        move_taken = 'y'
                    else:

                        move_taken = 'n'
        else:
            # randomly pick a position as long as it's not already taken
            move_taken = 'y'
            while move_taken == 'y':
                ai_move = random.randint(1, 9)
                if ai_move in spaces_taken:
                    move_taken = 'y'
                else:

                    move_taken = 'n'

    #once an open space is found return that value
    computer_move_count += 1
    print('The computer picked', ai_move)
    return ai_move

#have player select one or two player game.  Persist selection if they decide to play again.
def game_option():
    global new_game
    global game_selection

    valid_game = 'no'
    # check for valid reponse
    if new_game == 0:
        load_file()
        # show option for one or two player
        print('1. One player - Beginner')
        print('2. One player - Expert')
        print('3. Two player')
        print('4. Display High Scores')
        while valid_game == 'no':
            game_selection = input('Select a game type: ')
            try:
                game_selection = int(game_selection)
            except:
                print('Invalid selection')
                valid_game = 'no'
            else:
                if game_selection < 1 or game_selection > 4:
                    print('Invalid selection')
                    valid_game = 'no'
                else:
                    valid_game = 'yes'
    else:
        game_selection = game_selection


    return game_selection

def end_game():
    high_score()
    save_file()
    print('Thanks for playing')
    

def main():
    continue_game = 'y'
    global new_game
    global winning_player
    global player_1
    global player_2
    game_type = game_option()
    #one player game
    if game_type == 1 or game_type == 2:

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
            #smart_move(player_1)
            # player 1 moves
            player_move(player_1, select_move('one'))
            # show updated board
            display_board()
            # see if anyone won or game ended in draw
            continue_game = game_status(player_1, player_2)
            # computer moves if game is still going on
            if continue_game != 'n':
                player_move(player_2, computer_move(game_type))
                display_board()
                continue_game = game_status(player_1, player_2)

    #two player game
    elif game_type == 3:
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
    elif game_type == 4:
        display_score()
        #reset_game()
        main()
    #once game ends, see if user wants to play again
    score(game_type, winning_player)
    play_again = input('Would you like to play again (y or n)? ').lower()
    #check for invalid responses
    while play_again != 'y' and play_again != 'n':
        print('Only y or n are valid responses.')
        play_again = input('Would you like to play again (y or n)? ').lower()

    #start game over if they select yes
    if play_again == 'y':
        new_game = 1
        reset_game()
        main()
    #if they quit check for new high score and save top ten scores
    else:
       #check for high score and save top 10        
       
       end_game()
        
        

if __name__ == "__main__":
    main()
