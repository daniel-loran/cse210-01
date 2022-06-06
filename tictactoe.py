#Daniel Loran, Week 2 assignement, Tic Tac Toe

board = [
["-", "-", "-"],
["-", "-", "-"],
["-", "-", "-"]
]




def print_board(board):
  for row in board:
    for slot in row:
      print(f"{slot} ", end="")
    print()
      

      
def quit(player_input):
  if player_input.lower() == "q":
    print("Thanks for playing")
    return True
  else:
    return False
    
def check_input(player_input):
  if not isnum(player_input):
    return False
  if not bounds(player_input):
    return False
  return True


def isnum(player_input):
  if not player_input.isnumeric():
    print("This is not a valid number!")
    return False
  else:
    return True
   
def bounds(player_input):
  if int(player_input) < 1 or int(player_input) > 9:
    print("This number is out of bounds")
    return False
  else:
    return True

def istaken(coords, board):
    row = coords[0]
    col = coords[1]
    if board[row][col] != "-":
        print("This position is already taken.")
        return True
    else: return False
  
def coordinates(player_input):
    row = int(player_input / 3)
    col = player_input
    if col > 2:
      col = int(col % 3)
    return (row,col)
  
def add_to_board(coords, board, active_player):
    row = coords[0]
    col = coords[1]
    board[row][col] = active_player
    
      
def current_player(player):
  if player: return "x"
  else: return "o"


def win(player, board):
  if check_row(player, board): return True
  if check_col(player, board): return True
  if check_diag(player, board): return True
  return False

def check_row(player, board):
  for row in board:
    complete_row = True
    for slot in row:
      if slot != player:
        complete_row = False
        break
    if complete_row: return True
  return False

def check_col(player, board):
  for col in range(3):
    complete_col = True
    for row in range(3):
      if board[row][col] != player:
        complete_col = False
        break
    if complete_col: return True
  return False

def check_diag(player, board):
  if board[0][0] == player and board[1][1] == player and board[2][2] == player: 
    return True
  elif board[0][2] == player and board[1][1] == player and board[2][0] == player:
    return True
  else: return False

def main():
  player = True #True = x, False = o
  turns = 0
  while turns < 9:
      active_player = current_player(player)
      print_board(board)
      player_input = input("please enter position 1-9 or enter 'q' to quit: ")
      if quit(player_input):
         break
      if not check_input(player_input):
         print("please try again")
         continue
      player_input = int(player_input) - 1
      coords = coordinates(player_input)
      if istaken(coords, board):
       print("Please try again.")
       continue
      add_to_board(coords, board, active_player)
      if win(active_player, board):
       print(f"{active_player.upper()} won!")
       break


      turns += 1
      if turns == 9:
        print("it's a draw!")
      player = not player

if __name__ == "__main__":
    main()