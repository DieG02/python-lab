## HANDLING TABLES ##

print("\n")
print("## HANDLING TABLES ##")

def main():
  rows_input = input("Enter amount of rows: ")
  rows = int(rows_input)
  cols_input = input("Enter amount of cols: ")
  cols = int(cols_input)
  
  table = init(rows, cols)
  printf(table)
  convert(table)
  cross(table)
  extremes_h(table)
  extremes_v(table)
  sum(table)
  
def printf(table):
  print('\n')
  for _, arr in enumerate(table):
    row = ''
    for _, el in enumerate(arr):
      row += str(el) + " "
    print(row)

def init(m, n):
  matrix = [[0] * n for _ in range(m)]
  return matrix
  
def convert(table):
  for i, row in enumerate(table):
    for j in range(len(row)):
      table[i][j] = 1
  printf(table)

def cross(table):
  for i, row in enumerate(table):
    for j in range(len(row)):
      if i%2 == j%2:
        table[i][j] = 0
  printf(table)
  
def extremes_h(table):
  for j in range(len(table[0])):
    table[0][j] = 0
    table[-1][j] = 0
  printf(table)
  
def extremes_v(table):
  for i in range(len(table)):
    table[i][0] = 1
    table[i][-1] = 1
  printf(table)
  
def sum(table):
  acc = 0
  for _, row in enumerate(table):
    for _, el in enumerate(row):
      acc += el
  print(f"\n{acc}")

main()
print("\n")
