## LABYRINTH ##
import os

print("\n")
print("## LABYRINTH ##")
print("")

def main():
  print("Based on `maze.txt` we create a system wich allows you\nto see the possible movements of each position\n")
  base = os.path.join("lab_11/block_02", "utils", "test-03")
  filename = os.path.join(base, "maze.txt")
  corridors = get_corridors(filename)
    # Prettier, just for format porpuses
  keys = sorted(corridors.keys())
  flag = keys[0]
  for key in keys:
    if key[0] != flag[0]:
      flag = key
      print("")
    print(f"{key}  =  {corridors[key]}")
    
  
  
def get_corridors(filename: str):
  # NOTE: Complex implementation of type `dict[tuple, set]`
  corridors: dict[tuple, set] = dict()
  file = open(filename, "r")
  
  for i, line in enumerate(file):
    row = list(line.strip())
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

main()
print("\n")
