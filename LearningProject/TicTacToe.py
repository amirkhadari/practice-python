from numpy import transpose

class game:
    def design_game_board(self, size):
        # We use this formula to get the size of row and coloumn for the squared one
        row = (size * 3) + (size + 1)
        col = (size * 3) - (size - 1)
        # print(pipe)
        # running for loop to iterate the colomns
        for k in range(col):
            # if k is even then it prints dashes(-)
            if k % 2 == 0:
                # running for loop to generate dashes(-) for the game board
                for i in range(row):
                    # if row_num(i) are divisibles of 4, it print blank spaces
                    # else dashes '-'
                    # in pattern ' --- --- --- '
                    if i % 4 != 0:
                        print('-', end='')
                    else:
                        print(' ', end='')
                # using print statement to jump in new line
                print()
            # if k is odd then it prints PipeLine(|)
            else:
                # running for loop to generate PipeLine(|) for the game board
                for j in range(row):
                    if j % 4 == 0:
                        # if row_num(i) are divisibles of 4, it print PipeLine(|)
                        # else blank spaces
                        # in pattern '|   |   |   |'
                        print('|', end='')
                    else:
                        print(' ', end='')
                # using print statement to jump in new line
                print()

    # defining an function to check the game in rows and coloumns with argument inputs
    # of list of list[3 x 3] and using set to store unique values
    def line_game(self, row_col, line_set={}):
        # running for loop to check the elements in rows and appending to empty set
        # to store unique values
        for row_num in range(len(row_col)):
            play = set(row_col[row_num])
            # if length of set is equal to 1 and not equal to zero then
            # player of the row will win(either player 01 or 02)
            # returns the winning element
            if len(play) == 1 and len(play) != 0:
                return row_col[row_num][0]
        # if no condition satisfies, it returns zero
        return 0


        # if len(row_col) == len((row_col[0])):
        #     for row_num in range(len(row_col)):
        #         if row_col[row_num][0] == row_col[row_num][1] == row_col[row_num][2]:
        #             if row_col[row_num][0] != 0:
        #                 return row_col[row_num][0]
        #         if row_col[0][row_num] == row_col[1][row_num] == row_col[2][row_num]:
        #             if row_col[row_num][0] != 0:
        #                 row_col[row_num][0]

    # defining an function to check the game in diagonal with argument inputs
    # of list of list[3 x 3]

    def diagonal_game(self, diag):
        # function will work only when the center element should not equal to zero
        if diag[1][1] != 0:

            # checking both diagonal elements are same or not

            if diag[0][0] == diag[1][1] == diag[2][2]:
                return diag[1][1]
            elif diag[0][2] == diag[1][1] == diag[2][0]:
                return diag[1][1]

        # if condition doesn't satisfies then it will return zero
        return 0

if __name__ == "__main__":
    toe = game()
    # toe.design_game_board(4)

    # tic = [
    #     [2, 2, 0],
    #     [1, 1, 1],
    #     [1, 2, 1]
    # ]

    # creates an empty 3 * 3 list of lists with values 0
    brd = [[0 for col in range(3)] for row in range(3)]
    # initialize the var elm with value 1 to take the inputs
    # from the user 9 times(using while loop)
    elm = 1

    # loop will breaks if elm iterates more than 9

    while elm <= 9:

        # this will take user input in the form of row, col: 1,2 in range of 0 to 2 as string
        # using split() function in string split the values with ','
        # assign a value to get the index as one value to row and another to col
        play = input('please select a square to tick(in format row,col): ').split(',')
        row = int(play[0])
        col = int(play[1])

        # if the value at the mentioned index is 0, only then
        # player can enter his input
        # else it will do nothing and continue to the loop
        if brd[row][col] == 0:

            # Player 1 gets the value 1 and player to gets the value 2
            # always first chance given to player 1
            # by using logic even odd even goes for player 1
            brd[row][col] = 1 if elm % 2 != 0 else 2
            elm += 1
            print(brd)
        else:
            continue

        # once the iteration reaches to 5 it starts check the who wins the game
        # using pre defined methods line_game and diag_game

        if elm > 5 and elm <= 9 :

            # line_game will return the value of winning player if
            # game is completed in row and breaks the loop and declares the winner

            if toe.line_game(brd) > 0:
                # winner = row
                print(toe.line_game(brd), 'wins')
                break

            # by using transpose method in numpy we transpose the list
            # will check whether game is completed in colomns
            # if it completed then it returns winning player and breaks the loop
            # we use same line_game method to check the colomn game

            elif toe.line_game(transpose(brd)) > 0:
                # winner = col
                print(toe.line_game(transpose(brd)), 'wins')
                break

            # by using diagonal_game pre defined method we will check if
            # game is completed in diagonals or not, if it is completed
            # it will return the winning player and breaks the loop

            elif toe.diagonal_game(brd) > 0:
                # winner = diag
                print(toe.diagonal_game(brd), 'wins')
                break

            # if any above condition on the above are not satisfies
            # it will do nothing and again ask the user for input

            else:
                if elm <= 9:
                    continue
                else:
                    print('Game is Draw')
                    print('Game Over')

        # if user inputs are exceeded from 9 and no condition satisfies
        # declares game as draw and Game Over
        # else:
        #     print('Game Over')


