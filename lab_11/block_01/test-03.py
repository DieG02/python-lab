## SET HANDLING ##

print("\n")
print("## SET HANDLING ##")
print("")

ALPHABET = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

def main():
  print("We will show you some interesting tools")
  entry_1 = input("Provide a short string: ")
  entry_2 = input("Now other string to compare: ")
  
  set_1 = set(entry_1.upper())
  set_2 = set(entry_2.upper())
  alphabet = set(ALPHABET)
  
  case_1 = set_1.union(set_2)
  case_2 = set_1.difference(set_2)
  case_3 = alphabet.difference(case_1)
  
  print(f"\nUnion of all characters are:\n{case_1}")
  print(f"\nDifference between them are:\n{case_2}")
  print(f"\nDifference between all characters and alphabet:\n{case_3}")

main()
print("\n")
