## SECOND CHANCE ##
# NOTE: Logical missunderstanding, I thought it's valid 2 errors in the full loop, but you have 2 chances in each value

print("\n")
print("## SECOND CHANCE ##")
print("")

def is_float(value):
  try:
    float(value)  # Attempt to convert the string to a float
    return True   # If successful, it's a float
  except ValueError:
    return False  # If an error occurs, it's not a float
      
def main():
  stop = False
  tries = 2
  acc = 0
  
  # Each entry has at most 2 tries, so we restart it after a success entry
  while not stop and tries > 0:
    propmt = "Enter a float number: " if tries == 2 else "Reinsert the value: "
    entry = input(propmt)
    if is_float(entry):
      tries = 2
      acc += float(entry)
    elif entry != "":
      tries -= 1
      print(f"Invalid input, remain tries: {tries}\n")
    else:
      break
      
  print(f"The summary till now is {acc}")

main()
print("\n")
