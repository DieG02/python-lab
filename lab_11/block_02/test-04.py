## ARIANNA AND... ##
from module import get_corridors, output
import os

print("\n")
print("## ARIANNA AND... ##")
print("")

def main():
  print("Ariadne's thread owes its fame to the myth of Minos and the Labyrinth")
  print("So, now we will try to solve the labyrinth from `input.txt`\n")
  print("We have 3 stages for show how it works")
  case = input("Please enter a number [1-3]: ")
  
  base = os.path.join("lab_11/block_02", "utils", "test-04")
  filename = os.path.join(base, f"case_0{int(case)}.txt")
  corridors = get_corridors(filename)
  paths = get_paths(corridors)
  # prettier(paths)
  
  if paths:
    output(base, paths, int(case))
    
  return 
    
  
def get_paths(corridors: dict[tuple, set]) -> dict[tuple, str]:
  paths = dict()
  keys = corridors.keys()
  dataset = list()
  
  # Settings, hardcoded for confort
  height = 8
  width = 8
  
  # Set exits or default as "?"
  for key in keys:
    (y, x) = key
    paths[key] = {
      (0, x): "N",
      (y, width): "E",
      (height, x): "S",
      (y, 0): "W"
    }.get((y, x), "?")
    
    # Creates a virtual set with all possible values
    dataset += corridors[key]
    
  times = 0
  while len(dataset) > 0:
    for key in paths:
      if paths[key] != "?":
        continue
    
      (y, x) = key
      directions = {
        (y-1, x): "N",
        (y, x+1): "E",
        (y+1, x): "S",
        (y, x-1): "W"
      }
      
      for axis in directions:
        if axis in dataset and paths[axis] != "?":
          paths[key] = directions[axis]
          dataset.remove(key)
          dataset.remove(axis)
        
    # Here you can see how virtual set is changing after each iteration   
    # print(dataset, "\n")
    times += 1
  print(f"It takes {times} iterations for resolve the labyrinth\n")
  print("You can check the result in `solution` with your case number")
  return paths
  

main()
print("\n")
