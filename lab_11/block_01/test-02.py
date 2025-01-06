## TOP WORDS ##
import os

print("\n")
print("## TOP WORDS ##")
print("")

def main():
  print("Counts the words that appear most frequently `test-02/input.txt`\n")
  root = os.path.join("lab_11/block_01", "utils", "test-02")
  file = open(root + "/input.txt", "r")
  counter = dict()
  
  for line in file:
    row = line.strip().split(" ")
    for word in row:
      filtered = ''.join([char for char in word if char.isalpha()])
      if len(filtered) < 4:
        continue
      if filtered in counter:
        counter[filtered] += 1
      else:
        counter[filtered] = 1
        
  sorted_words = sorted(counter.items(), key=lambda item: item[1], reverse=True)
  # NOTE: Here we get a `tuple` after the sort process, like (word, count)
  ranking = sorted_words[:5]
  
  print(f"{'WORD':<20} {'COUNTER'}")
  # print(type(ranking[0])) # => `tuple`
  for pair in ranking:
    print(f"{pair[0]:<20} {pair[1]}")

main()
print("\n")
