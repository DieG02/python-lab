import os
# from typing import TextIO

def snail_loop(matrix: list[list[int]], callback):
  m = len(matrix)
  n = len(matrix[0])
  
  # Initial values
  count = 1 # Number to print
  position = 0 # Top = 0, Right = 1, Bottom = 2, Left = 3
  i = 0; j = 0 # Pointers
  
  print(matrix)
  print("\n")
  
  while count < m*n:
    matrix[i][j] = count # Set number
    direction = position % 4 # Get direction
    
    # Rules for validate direction
    top    = j+1 < m  and matrix[i][j+1] == 0
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
  
    callback(i, j)

def hash_lop(matrix: list[list[int]], callback):
  height = len(matrix)
  width = len(matrix[0])
  for i, row in enumerate(matrix):
    for j in range(len(row)):
      callback(i, j)
      callback(width - i, j)
      callback(width - i, height - j)
      callback(i, height - j)
    
def get_corridors(filename: str) -> dict[tuple, set]:
  # NOTE: Complex implementation of type `dict[tuple, set]`
  corridors: dict[tuple, set] = dict()
  file = open(filename, "r")
  
  for i, line in enumerate(file):
    # We cannot use `list.strip()` in this case because the labyrinth use " " as roads
    row = list(line.split("\n")[0])
    for j, ch in enumerate(row):
      if ch == "*":
        continue
      
      # Pair of tuples
      current = (i, j) # Only if we found " "
      top = (i+1, j)
      right = (i, j+1)
      bottom = (i, j-1)
      left = (i-1, j)
      
      if current not in corridors:
        corridors[current] = set()
        
      # Verify top, right, bottom, left
      for direction in [top, right, bottom, left]:
        if direction in corridors:
          corridors[current].add(direction)
          corridors[direction].add(current)
      
  return corridors

def prettier(corridors: dict[tuple, set]) -> None:
  keys = sorted(corridors.keys())
  flag = keys[0]
  for key in keys:
    if key[0] != flag[0]:
      flag = key
      print("")
    print(f"{key}  =  {corridors[key]}")

def output(base: str, paths: dict[tuple, set[tuple]], case: str) -> None:
  with open(os.path.join(base, f"case_0{int(case)}.txt"), "r") as file:
    template = ""
    for i, line in enumerate(file):
      row = list(line)
      for j, ch in enumerate(row):
        if (i, j) in paths:
          row[j] = paths[(i, j)]
          
      template += f"{''.join(row)}"
      
  with open(os.path.join(base, f"solution_0{int(case)}.txt"), "w") as file:
    file.write(template)