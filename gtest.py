# goal_test method definition
def goal_test(board):
  for i in range(len(board)):               # i => row
    #print(f"Row {i}")
    for j in range(len(board[i])):          # j => column
      #print(f"Column {j}")
      if (board[i][j] == True):
        if (not(check_row(board, i, j)) or 
        not(check_column(board, i, j)) or 
        not(check_left_diagonal(board, i, j)) or 
        not(check_right_diagonal(board, i, j))):
          print(f"Goal test failed at: [{i}, {j}]")
          return False
  
  return True
# end goal_test mehtod definition



# check entire row for more than one existance of queen 
def check_row(board, row, column):
  n = len(board[row])
  for j in range(n):                      # iterate over the columns of the given row
    if (board[row][j] and j != column):
      return False
  return True
# end check_row method


# check entire column for more than one existance of queen 
def check_column(board, row, column):
  n = len(board)
  for i in range(n):                      # iterate over the rows of the given column
    if (board[i][column] and i != row):
      return False
  return True
# end check_column method


# get starting point of the left diagonal with respect to the queen position
def get_left_diagonal_start(board, row, column):    # left diagonal => /
  # your code here...
  i = row
  j = column

  while (i != 0 and j != (len(board[row])-1)):
    i -= 1
    j += 1
  
  LD_start_point = [i, j]

  return LD_start_point
# end get_left_diagonal_start fucntion


# get starting point of the right diagonal with respect to the queen position
def get_right_diagonal_start(row, column):    # right diagonal => \
  # your code here...
  i = row
  j = column

  while (i != 0 and j != 0):
    i -= 1
    j -= 1
  
  RD_start_point = [i, j]

  return RD_start_point
# end get_right_diagonal_start fucntion


# check left diagonal for more than one existance of queen 
def check_left_diagonal(board, row, column):
  diagonal_start_point = get_left_diagonal_start(board, row, column)  
  
  s_i = diagonal_start_point[0]        # s_i => starting row for diagonal with respect to the given queen position
  s_j = diagonal_start_point[1]        # s_j => starting column for diagonal with respect to the given queen position

  i = s_i
  j = s_j
  
  while (i < len(board) and j >= 0):
    if (board[i][j] and (i != row and j != column)):
      return False

    i += 1
    j -= 1

  return True
# end check_left_diagonal method


# check right diagonal for more than one existance of queen 
def check_right_diagonal(board, row, column):
  diagonal_start_point = get_right_diagonal_start(row, column)  

  s_i = diagonal_start_point[0]      # s_i => starting row for diagonal with respect to the given queen position
  s_j = diagonal_start_point[1]      # e_j => starting column for diagonal with respect to the given queen position
  

  i = s_i
  j = s_j
  while (i < len(board) and j < len(board[i])):
    if (board[i][j] and (i != row and j != column)):
      return False
    
    i += 1
    j += 1
  return True
# end check_right_diagonal method


