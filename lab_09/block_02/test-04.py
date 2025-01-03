## NUMERICAL SUCCESSION ##
# NOTE:
# We didn't use an exit sentence, so we cut one item before fill the matrix and then we add it manually
# Also, we use `init` to generate a default numerical `matrix` and `printf` for a prettier print

print("\n")
print("## NUMERICAL SUCCESSION ##")
print("")

def init(m, n):
  return [[0] * n for _ in range(m)]

def printf(table):
  print("")
  for _, arr in enumerate(table):
    row = ""
    for _, el in enumerate(arr):
      row += f"{str(el):^5}"
    print(row)

def main():
  # Settings
  n_input = input("Enter a number to draw a matrix: ")
  n = int(n_input)
  matrix = init(n, n)
  # printf(matrix)

  # Initial values
  count = 1 # Number to print
  position = 0 # Top = 0, Right = 1, Bottom = 2, Left = 3
  i = 0; j = 0 # Pointers
  
  while count < n*n:
    matrix[i][j] = count # Set number
    direction = position % 4 # Get direction
    
    # Rules for validate direction
    top    = j+1 < n  and matrix[i][j+1] == 0
    right  = i+1 < n  and matrix[i+1][j] == 0
    bottom = j-1 >= 0 and matrix[i][j-1] == 0
    left   = i-1 >= 0 and matrix[i-1][j] == 0
    
    # Custom switch, only one per round is valid
    if direction == 0 and top:
      count += 1
      j += 1
    elif direction == 1 and right:
      count += 1
      i += 1
    elif direction == 2 and bottom:
      count += 1
      j -= 1
    elif direction == 3 and left:
      count += 1
      i -= 1
    else:
      position += 1
  
  matrix[i][j] = count
  printf(matrix)
        
main()
print("\n")