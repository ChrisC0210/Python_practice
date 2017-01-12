'''
    7.Lists and Functions
    小遊戲，隨機定義一格作為目標
    猜三次看猜不猜的到
'''
from random import randint
#引入隨機BIF

board = []
for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print(" ".join(row))

print ("Let's play Battleship!")
print_board(board)
'''
O O O O O
O O O O O
O O O O O
O O O O O
O O O O O
'''
#定義隨機質
def random_row(board):
    return randint(0, len(board) - 1)
    #一行五個，從0開始
def random_col(board):
    return randint(0, len(board[0]) - 1)
    #總共有幾列，因為是多維陣列所以只取第一行來判斷
    
for turn in range(4):
    if turn ==3:
        print("")
        print ("Game Over")
    else:
        print ("Turn", turn + 1)
        ship_row = random_row(board)
        ship_col = random_col(board)
        print (ship_row)
        print (ship_col)
        # Everything from here on should go in your for loop!
        # Be sure to indent four spaces!
        guess_row = int(input("Guess Row:"))
        guess_col = int(input("Guess Col:"))

        if guess_row == ship_row and guess_col == ship_col:
            print ("Congratulations! You sunk my battleship!")
            print("My battleship is in")

            print("")
            break
        else:
            if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
                print ("Oops, that's not even in the ocean.")
            elif(board[guess_row][guess_col] == "X"):
                print ("You guessed that one already.")
            else:
                print ("You missed my battleship!")
                board[guess_row][guess_col] = "X"
                print("My battleship is in")
                print("")
            # Print (turn + 1) here!
            print_board(board)
