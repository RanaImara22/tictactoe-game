#ID: 20210132
#NAME: Rana Taha Hassan Mohamed
#DATE: 10/3/2022


# Will hold our game board data
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

boardLog = [0, 0, 0,
            0, 0, 0,
            0, 0, 0]

# Lets us know if the game is over yet
game_still_going = True

# Tells us who the winner is
winner = None
global current_player
current_player= "odd_player"


list=[0,1,2,3,4,5,6,7,8,9]

# ------------- Functions ---------------

# Play a game of tic tac toe
def play_game():
    display_board()

    # Loop until the game stops (winner or tie)
    while game_still_going:
        # Handle a turn
        turns()

        # Check if the game is over
        check_if_game_over()

        # Flip to the other player
        flip_player()

    # Since the game is over, print the winner or tie
    if winner == "odd_player" or winner == "even_player":
        print(winner , " won.")
    elif winner == None:
        print("Tie.")


def display_board():
    print("\n")
    print(board[0], " | ", board[1], " | ", board[2], "     1 | 2 | 3")
    print(board[3], " | ", board[4], " | ", board[5], "     4 | 5 | 6")
    print(board[6], " | ", board[7], " | ", board[8], "     7 | 8 | 9")
    print("\n")


def move(position, x2):
    board[x2] = position
    boardLog[x2] = 1
    display_board()


def odd(x, x2):
    while (x % 2 == 0 or x > 10 or x < 1):
        x = int(input('enter an odd number'))
    move(x, x2)


def even(x, x2):
    while (x % 2 != 0 or x > 10 or x < 0):
        x = int(input('enter an even number'))

    move(x, x2)


def turns():
    # Get position from player
    global current_player
    print(current_player + "'s turn.")
    position = input("Choose a position from 1-9: ")
    while True:
        x = int(input('enter a number to add on board: '))
        if x in list:
            list.remove(x)
            break
        else :
            print("you can use each number only once!")
            continue



    # Whatever the user inputs, make sure it is a valid input, and the spot is open
    valid = False
    while not valid:

        # Make sure the input is valid
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Choose a position from 1-9: ")

        # Get correct index in our board list
        position = int(position) - 1

        # Then also make sure the spot is available on the board
        if board[position] == "-":
            valid = True
        else:
            print("You can't go there. Go again.")

    # Put the game piece on the board
    board[position] = x
    if current_player == "odd_player":
        odd(x, position)
    else:
        even(x, position)
    # Show the game board
    display_board()


# Check if the game is over
def check_if_game_over():
    check_for_winner()
    check_for_tie()


# Check to see if somebody has won
def check_for_winner():
    if (boardLog[0] + boardLog[1] + boardLog[2] == 3):
        if (board[0] + board[1] + board[2] == 15):
            print(f"{current_player} won!")
            exit()
    if (boardLog[0] + boardLog[3] + boardLog[6] == 3):
        if (board[0] + board[3] + board[6] == 15):
            print(f"{current_player} won!")
            exit()

    if (boardLog[1] + boardLog[4] + boardLog[7] == 3):
        if (board[1] + board[4] + board[7] == 15):
            print(f"{current_player} won!")
            exit()
    if (boardLog[3] + boardLog[4] + boardLog[5] == 3):
        if (board[3] + board[4] + board[5] == 15):
            print(f"{current_player} won!")
            exit()
    if (boardLog[2] + boardLog[5] + boardLog[8] == 3):
        if (board[2] + board[5] + board[8] == 15):
            print(f"{current_player} won!")
            exit()
    if (boardLog[6] + boardLog[7] + boardLog[8] == 3):
        if (board[6] + board[7] + board[8] == 15):
            print(f"{current_player} won!")
            exit()

    else:
        return False


# Check if there is a tie
def check_for_tie():
    # Set global variables
    global game_still_going
    # If board is full
    if "-" not in board:
        game_still_going = False
        return True
    # Else there is no tie
    else:
        return False


def flip_player():
    global current_player

    if current_player == "odd_player":
        current_player = "even_player"

    elif current_player == "even_player":
        current_player = "odd_player"


# ------------ Start Execution -------------
# Play a game of tic tac toe
play_game()
