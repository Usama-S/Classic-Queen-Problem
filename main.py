from gtest import goal_test


# ========== correct board => goal test should pass

# board = [
#   [False, False, False, False, True, False, False, False],
#   [False, True, False, False, False, False, False, False],
#   [False, False, False, True, False, False, False, False],
#   [False, False, False, False, False, False, True, False],
#   [False, False, True, False, False, False, False, False],
#   [False, False, False, False, False, False, False, True],
#   [False, False, False, False, False, True, False, False],
#   [True, False, False, False, False, False, False, False]
#   ]


# ========== wrong board => goal test should fail

board = [
  [False, False, False, False, False, False, False, True],
  [False, True, False, False, False, False, False, False],
  [False, False, False, True, False, False, False, False],
  [False, False, False, False, False, False, True, False],
  [False, False, True, False, False, False, False, False],
  [False, False, False, False, False, False, False, True],
  [False, False, False, False, False, True, False, False],
  [True, False, False, False, False, False, False, False]
  ]



#print(len(board))
#print(len(board[0]))

# call goal test method
if (goal_test(board)):
  print("Goal test passed!")
else:
  print("Goal test failed!")