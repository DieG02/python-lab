## TIC-TAC-TOE ##
import utils

print("\n")
print("## TIC-TAC-TOE ##")

empty = "-"
def main():
  board = init()
  utils.prints(board)
  winner = False
  index = 0
  
  while index < 9 and not winner:
    print("\nEach movement must to be like this `0 0` (row, col)\n")
    player = index%2 + 1
    position = input(f"Player {player} moves: ")
    r, c = position.split()
    
    valid = movement(board, r, c, "X" if player == 1 else "O")
    winner = match(board, player)
    
    if valid:
      utils.prints(board)
      index += 1

# Inits a new board, once per match
def init():
  rows, cols = 3, 3
  board = [[empty for _ in range(cols)] for _ in range(rows)]
  return board

# Base on the player, make a movement with the enter position
def movement(board, r, c, move):
  row, col = int(r), int(c)
  if board[row][col] == empty:
    board[row][col] = move
    return True
  else:
    print("It's not a valid movement")
    print("Current board state")
    utils.prints(board)
    return None

# Look for a winner of the match after a movement
def match(board, player):
  flag = False
  for i in range(3):
    row = board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][1] != empty
    col = board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[1][i] != empty
    d_1 = board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[1][1] != empty
    d_2 = board[2][0] == board[1][1] and board[1][1] == board[0][2] and board[1][1] != empty
    if row or col or d_1 or d_2:
      print(f"Player {player} wins!")
      flag = True
      
  return flag

main()
print("\n")
