## COVALENT BONDS ##
import os

print("\n")
print("## COVALENT BONDS ##")
print("")

def main():
  print("Welcome to Chemistry Bot")
  print("You can look for `Bond`, `Bond energy` or `Bond length`")
  entry = input("Enter a value and I'll do the rest: ")
  root = os.path.join("lab_10/block_02", "utils", "test-04")
  results: list[str] = list()
  
  with open(os.path.join(root, "bond_data.txt"), "r") as file:
    for row in file:
      if entry in row:
        results.append(row.strip())
  
  if len(results) == 1:
    print("\nThis is the only result found\n")
  elif len(results) > 1:
    print("\nThese are the results found\n")
  else:
    print("\nThere are no results for {entry}, try another\n")
    
  for result in results:
    [bond, energy, length] = result.split(' ')
    print(f"{bond:^8} {energy:<5} {length:<5}")

main()
print("\n")
