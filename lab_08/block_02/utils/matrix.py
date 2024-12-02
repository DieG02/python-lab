def printf(table):
  print('\n')
  for _, arr in enumerate(table):
    row = ''
    for _, el in enumerate(arr):
      row += f"{str(el):<4}"
    print(row)
    
def prints(board):
  print('\n')
  for _, arr in enumerate(board):
    row = ''
    for _, el in enumerate(arr):
      row += f"{str(el):<4}"
    print(row, "\n")