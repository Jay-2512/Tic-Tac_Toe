#--variables--#

player_rn = "X"
game_running = True
# main board
board = ["-","-","-",
         "-","-","-",
         "-","-","-"]

#display board :

def display_board():
    print(board[0] + " | " + board [1] + " | " + board[2])
    print(board[3] + " | " + board [4] + " | " + board[5])
    print(board[6] + " | " + board [7] + " | " + board[8])

def player_turns(player):
    print(player + "\'s turn ")
    position = input("Enter the position : (1-9) :: ")

    valid = False


    while not valid:

        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                position = input("!! Invalid input !! Enter the position : (1-9) :: ")
        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            print("You can't go there go again!")

    board[position] = player
    display_board()



# main game function
def main_game():
    # printing the board :
    display_board()
    while game_running:
        # player turns :
        player_turns(player_rn)
        check_winner()
        switch_turn()

    if winner == "X" or winner == "O":
        print(winner + " Won.")
    elif winner == None:
        print("The Game is a Tie.")



def check_game_finish():
    check_winner()
    check_gametie()


# Checking for winner
def check_winner():

    # global variabe

    global winner

    row_winner = check_row()
    column_winner = check_column()
    diagonal_winner = check_diagonal()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None

    return

def check_row():

    # global

    global game_running

    row1 = board[0] == board[1] == board[2] != "-"
    row2 = board[3] == board[4] == board[5] != "-"
    row3 = board[6] == board[7] == board[8] != "-"

    if row1 or row2 or row3 :
        game_running = False
    if row1:
        return board[0]
    if row2:
        return board[3]
    if row3:
        return board[6]

def check_column():

    # global

    global game_running

    column1 = board[0] == board[3] == board[6] != "-"
    column2 = board[1] == board[4] == board[7] != "-"
    column3 = board[2] == board[5] == board[8] != "-"

    if column1 or column2 or column3:
        game_running = False

    if column1:
        return board[0]
    if column2:
        return board[1]
    if column3:
        return board[2]

def check_diagonal():

    # global

    global game_running

    diag1 = board[0] == board[4] == board[8] != "-"
    diag2 = board[2] == board[4] == board[6] != "-"

    if diag1 or diag2:
        game_running = False

    if diag1:
        return board[0]
    if diag2:
        return board[2]


# switch player_turns

def switch_turn():
    global player_rn

    if player_rn == "X":
        player_rn = "O"
    else:
        player_rn = "X"

    return

def check_gametie():
    global game_running
    if "-" not in board:
        game_running = False
    return

main_game()
# mainboard
# main game function
# player turns
# win // lose
# check win
# players
