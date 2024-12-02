## MAGIC SQUARE ##
import random
from utils import printf

print("\n")
print("## MAGIC SQUARE ##")


def main():
  # rows, cols = 3, 3
  # square = [[random.randint(1, rows * cols) for _ in range(cols)] for _ in range(rows)]
  magic = [[16, 3, 2, 13], [4, 10, 11, 8], [9, 6, 7, 12], [4, 15, 14, 1]]
  magic_square(magic)
  printf(magic)

def magic_square(table):
  row = 0
  col = 0
  d_1 = 0
  d_2 = 0
  is_magic = True
  
  for i in range(len(table)):
    acc_row = 0
    acc_col = 0
    for j in range(len(table)):
      if i == 0:
        row += table[i][j]
        col += table[j][i]
      else:
        acc_row += table[i][j]
        acc_col += table[j][i]
      if i == j:
        d_1 += table[i][j]
        d_2 += table[len(table) - i - 1][j]
      
    if acc_row != row and i != 0 and acc_col != col:
      is_magic = False
      break
  
  if is_magic:
    print("\nIt's a magic square\n")
  else:
    print("\nIt's not a magic square\n")
    
  print(f"Magic row: {acc_row}")
  print(f"Magic col: {acc_col}")
  print(f"Diagonals: {d_1}, {d_2}")
  
main()
print("\n")
