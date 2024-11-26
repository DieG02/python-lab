## ALTER SIGNS ##

print("\n")
print("## ALTER SIGNS ##")

def main():
  acc = 0; flag = True

  while True:
    num_input = input("Enter a number (or press Enter to stop): ")
    
    if num_input == "":
      break

    try:
      num = int(num_input)
      acc += num if flag else -num
      flag = not flag
      print(f"The count is now {acc}")
      
    except ValueError:
      print("Please enter a valid number.\n")
      continue

main()
print("\n")
