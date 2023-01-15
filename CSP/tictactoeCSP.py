import random
import copy

PLAYER_1 = 2
PLAYER_AI = 1
global Current_player


def printSolution(board):
    """Print Tic Tac Toe board
    """
    for i in range(3):
        for j in range(3):
            print(board[i][j], end=' ')
        print()


def is_end(board):
    if Is_board_full(board):
        print("Match could not be solved. Nobody won")
        raise Exception("Game Over")
    # Vertical win
    for i in range(0, 3):
        if (board[0][i] != 0 and
            board[0][i] == board[1][i] and
                board[1][i] == board[2][i]):
            return board[0][i]
            # return True

    # Horizontal win
    for i in range(0, 3):
        if (board[i] == [1, 1, 1]):
            return 1
        elif (board[i] == [2, 2, 2]):
            return 2
            # return True

    # Main diagonal win
    if (board[0][0] != 0 and
        board[0][0] == board[1][1] and
            board[0][0] == board[2][2]):
        return board[0][0]
        # return True

    # Second diagonal win
    if (board[0][2] != 0 and
        board[0][2] == board[1][1] and
            board[0][2] == board[2][0]):
        return board[0][2]
        # return True

    return 0


def is_safe(board):

    for i in range(0, 3):
        for j in range(0, 3):
            board2 = copy.deepcopy(board)
            if board2[i][j] == 0:
                board2[i][j] = 2
                # verticle win
                for k in range(0, 3):
                    if (board2[0][k] == 2 and
                        board2[0][k] == board2[1][k] and
                            board2[1][k] == board2[2][k]):

                        return False
                # horizontal win
                for k in range(0, 3):
                    if (board2[k] == [2, 2, 2]):
                        return False

                # Main diagonal win
                if (board2[0][0] == 2 and
                    board2[0][0] == board2[1][1] == 2 and
                        board2[0][0] == board2[2][2] == 2):
                    return False

                # Second diagonal win
                if (board2[0][2] == 2 and
                    board2[0][2] == board2[1][1] == 2 and
                        board2[0][2] == board2[2][0] == 2):
                    return False

                board2[i][j] = 0

    return True


def is_valid(px, py, board):
    if px < 0 or px > 2 or py < 0 or py > 2:
        return False
    elif board[px][py] != 0:
        return False
    else:
        return True


def Is_board_full(board):
    # Is the whole board full?
    for i in range(0, 3):
        for j in range(0, 3):
            # There's an empty field, we continue the game
            if (board[i][j] == 0):
                return False

    return True


def CSP(board, count=0, Current_player=None, winner=None):
    if Is_board_full(board):
        raise Exception("Match could not be solved. Nobody won")
    flag1 = 0
    flag2 = 0
    printSolution(board)
    print()
    while winner == False:
        if Current_player == 2:
            while (True):
                player = is_end(board)
                if player != True:
                    px = int(input('Insert the X coordinate: '))

                    py = int(input('Insert the Y coordinate: '))
                    if is_valid(px, py, board):
                        board[px][py] = 2
                        printSolution(board)
                        print()
                        Current_player = 1
                        break
                    else:
                        print('The move is not valid! Try again.')
                elif is_end(board) == 3:
                    print("Nobody won.")
                else:
                    flag1 += 1
                    if flag1 <= 1:
                        winner = True
                        break
                    else:
                        break
        else:
            while (True):
                player = is_end(board)
                if player != True:
                    px = random.randint(0, 2)
                    py = random.randint(0, 2)
                    if is_valid(px, py, board):
                        board[px][py] = 1
                        printSolution(board)
                        if is_end(board):
                            winner = True
                            break
                        if is_safe(board) != True:
                            print()
                            print(count)
                            print()
                            if count > 900:
                                print("The problem cannot be solved. Winner is 2")
                                raise Exception(
                                    "Game over")
                            board[px][py] = 0
                            CSP(board, count=count+1,
                                Current_player=1, winner=winner)
                        print()
                        printSolution(board)
                        Current_player = 2
                        break
                else:
                    flag2 += 1
                    if flag2 <= 1:
                        winner = True
                        break
                    else:
                        winner = True
                        break
    if winner == True:
        winner = is_end(board)
        print(f"The winner is {winner}")
        raise Exception("Game is Finished.")


def solveGame():

    board = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    print(CSP(board, Current_player=2, winner=False))


solveGame()
