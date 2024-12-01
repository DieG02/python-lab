## SPACING ##
# COMMENT: I doubt it is a good solution but it is solid, it holds quite a bit without breaking the pattern. The only issue is that of the reverse, which is forced to be as I wanted it to be.

print("\n")
print("## SPACING ##")
empty = " "; fill = "#"

def main():
  position_input = input("Enter the ammount of spaces in the car park: ")
  position = int(position_input)
  row = []
  for _ in range(position): 
    row.append(empty)
  sort_car(row)

def sort_car(row):
  i = 0
  while i < len(row):
    slice = list() # 10
    acc = list()
    
    # Separate into short arrays
    for j, el in enumerate(row):
      if el == ' ': 
        acc.append(j)
      elif el == fill:
        slice.append(acc) if len(acc) > 0 else None
        acc = list()
    slice.append(acc)
    
    # I didn't get my original solution, so with this it's actually the same
    slice.reverse()

    # Get maximum space
    max_slice = [],
    for k in range(len(slice)):
      if len(slice[k]) >= len(max_slice):
        max_slice = slice[k]
    
    # Add "X" in the center 
    length = len(max_slice)
    long = round(length/2 if length%2 == 0 else (length-1)/2)
    index = max_slice[long]
    row[index] = fill
    print(row)
    i+=1


main()
print("\n")