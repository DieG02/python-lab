## WORDS COUNTER ##
import os
# NOTE: `os` it's not necessary for open a file, 
# and `with open(url)` it's not the only way

print("\n")
print("## WORDS COUNTER ##")
print("")

def main():
  print("Counts all the words from `test-01/input.txt`\n")
  root = os.path.join("lab_11/block_01", "utils", "test-01")
  file = open(root + "/input.txt", "r")
  counter = dict()
  
  for line in file:
    row = line.strip().split(" ")
    for word in row:
      filtered = ''.join([char for char in word if char.isalpha()])
      if filtered in counter:
        counter[filtered] += 1
      else:
        counter[filtered] = 1
  
  print(f"{'WORD':<20} {'COUNTER'}")
  for key in counter:
    print(f"{key:<20} {counter[key]}")

main()
print("\n")
