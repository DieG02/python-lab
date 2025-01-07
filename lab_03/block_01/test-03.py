## HANDLING STRINGS ##

print("\n")
print("## HANDLING STRINGS ##")

def analyise():
  print("Today I'll show how handle strings and some interesting tools")
  print("For this exercise, we'll play with DNA, so...")
  print("A DNA sequence is composed by 'A', 'C', 'T' and 'G'\n")
  
  long = input("Enter a long DNA sequence [20 characters]: ")
  short = input("Now another shorter [3 characters]: ")
  
  is_inside = short in long
  index = long.find(short) # Return -1 if not
  # We store the values of len of the separation if exists
  times = len(long.split(short)) - 1
  
  if is_inside:
    print(f"\nWe found the value at position: {index}, but it appears in total: {times}")
  else:
    print(f"\n{short} it's not inside {long}")
  return

analyise()
print("\n")
