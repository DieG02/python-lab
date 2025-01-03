## BOOK A SEAT IN A THEATER ##

print("\n")
print("## BOOK A SEAT IN A THEATER ##")
print("")

def get_matrix():
  matrix = [
    [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
    [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
    [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
    [10, 10, 20, 20, 20, 20, 20, 20, 10, 10],
    [10, 10, 20, 20, 20, 20, 20, 20, 10, 10],
    [10, 10, 20, 20, 20, 20, 20, 20, 10, 10],
    [20, 20, 30, 30, 40, 40, 30, 30, 20, 20],
    [20, 30, 30, 40, 50, 50, 40, 30, 30, 20],
    [30, 40, 50, 50, 50, 50, 50, 50, 40, 20]
  ]
  return matrix

def printf(matrix: list[list[int]]) -> None:
  print("")
  for _, el in enumerate(matrix):
    print(el)
  print("\n")

def main():
  matrix = get_matrix()
  flag = True
  while flag:
    # Python creates a copy if we pass `flag` as a param, so we must to update in this scope with the return value of `fill` function
    flag = fill(matrix, flag)
    printf(matrix)


def fill(matrix: list[list[int]], flag: bool) -> None:
  entry = input("Enter a `row,col` or `price` or `E` for exit for book a seat: ")
  # 1,1 / 50 / E
  is_map = entry.find(',')
  
  # With this condition, we check if there is a (x, y) couple or not
  if is_map != -1:
    map = entry.split(",")
    # Seats start at `1,1`` for the user, for us at `0,0`
    row, col = [int(map[0]) - 1, int(map[1]) - 1]
    if matrix[row][col] == 0:
      print("This seat is not longer available, try another one")  
    else:  
      matrix[row][col] = 0
      print(f"Your seat is booked on row {i}, col {j}")
    return True
    
  elif entry.isnumeric():
    price = int(entry)
    full = True
    for i, arr in enumerate(matrix):
      for j, el in enumerate(arr):
        if price == el:
          print(f"Your assigned seat is on row {i}, col {j}")
          matrix[i][j] = 0
          return True
        
        # Check if there is at least one more seat, it's optimized for once
        if full and matrix[i][j] != 0:
          full = False
    if full:
      print("The theater is full, we so sorry but you cannot book more a seat")
    else:
      print("There are no more seat for this price, try another one")  
    return not full
    
  else:
    print("Program finished")
    return  False
  
main()
print("\n")
