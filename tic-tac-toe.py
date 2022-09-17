"""
CSE210 Week 01 prove: Tic-Tac-Toe
Written by Graham McClure.
"""
def main():
    # list of numbers of where
    o_moves = []
    x_moves = []
    
    # false for X, true for O
    turn = True

    loop = True
    while loop:
        # toggle turn
        turn = toggle(turn)
        # check whose turn it is
        if turn == False:
            turn_label = "x"
        else: turn_label = "o"

        # draw the board
        print()
        draw_board(x_moves, o_moves)
        # checks if game has concluded
        gameover = check_win(x_moves, o_moves)
        
        # if game has not concluded
        if not gameover:
        
            # input request loop
            invalid = True
            while invalid:
                # input move location
                move = int(input(f"{turn_label}'s turn to choose a square (1-9): "))
                # if square is open
                if  move not in x_moves and move not in o_moves and move < 10 and move > 0:
                    # release loop
                    invalid = False
                # invalid move
                else: print("Invalid location.")
            # append move to o or x
            if turn == False: x_moves.append(move)
            else: o_moves.append(move)
        
        # if game has concluded
        else:
            loop = False
        

def draw_board(x, o):
    """Draws the tic-tac-toe board"""
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # replace numbers with o
    for i in range(len(o)):
        # replace with O
        nums[o[i]-1] = "o"
    # replace numbers with X
    for i in range(len(x)):
        # replace with X
        nums[x[i]-1] = "x"
        
    # from 0 to 9 in steps of 3, print out the board
    for i in range(0, 9, 3):
        print(f"{nums[i]}|{nums[i+1]}|{nums[i+2]}\n-+-+-")

def toggle(variable):
    """Toggles a variable from true to false, or vice versa."""
    if variable == True:
        return False
    elif variable == False:
        return True
    else: raise Exception("Invalid toggle argument")

def check_win(x, o):
    """Compares moves made from X and O to the winning combinations.
    Returns True if gameover, else returns False."""

    # all possible winning move combinations
    win_req = [[1, 2, 3], [4, 5, 6], [7, 8, 9], # horizontal
        [1, 4, 7], [2, 5, 8], [3, 6, 9], # vertical
        [1, 5, 9], [3, 5, 7]] # diagonal
    
    gameover = False

    # check for win
    # run through each group in win_req
    for i in range(2):
        # determine current player
        if i == 0:
            player_list = o
            player_label = "O"
        else: 
            player_list = x
            player_label = "X"

        for j in range(len(win_req)):
            # reset the correct numbers counter
            correct = 0
            # run through the 3 items in the group in win_req
            for k in range(3):
                # if the current item is in it
                if win_req[j][k] in player_list:
                    # add 1
                    correct += 1
            if correct == 3:
                print(f"{player_label} Wins")
                gameover = True
                break
    # game ends in draw
    if len(o) + len(x) == 9:
        print("The game was a Draw!")
        gameover = True
    return gameover

main()
input("\nPress Enter to close.\n")