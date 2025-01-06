## CENSORED TEXT ##
# NOTE: I don't have idea why I cannot use `items` in the same way of `file`
# I thought because we cannot have 2 files open at the same time but not
# Also if I do `items = items.strip()` inside doesn't matter,
# Always display only the first row of the file
import os

print("\n")
print("## CENSORED TEXT ##")
print("")

def main():
  print("We have a `raw_text.txt` file that we want to censored for testing porpuses")
  print("So, the result will store at `censored_text.txt`")
  print("You can take a look if you want\n")

  root = os.path.join("lab_11/block_01", "utils", "test-04")
  
  items = os.path.join(root, "bad_words.txt") # open(root + "/bad_words.txt", "r")
  file = os.path.join(root, "raw_text.txt") # open(root + "/raw_text.txt", "r")
  result = get_censored_text(file, items)
  
  with open(root + "/censored_text.txt", "w") as clean_text:
    clean_text.write("".join(result))
    
  
    
def get_censored_text(file_url: str, items_url: str) -> list[str]:
  """
  file: Path to the text to be censored
  items: Path to the bad words to censure
  return: Text to be store at a clean .txt file
  """
  template = list()
  swearword = open(items_url, "r")
  items = [word.strip() for word in swearword]
  swearword.close()
  
  file = open(file_url, "r")
  
  for i, line in enumerate(file):
    row = line.strip()
    for item in items:
      if item in row:
        print(f"line: {i:<4} item: {item:<10}")
        start = row.index(item)
        length = len(item)
        end = start + length
        splitted = list(row)
        splitted[start:end] = ["*" for _ in range(length)]
        row = "".join(splitted)
    
    template.append(f"{row}\n")    
  return template

main()
print("\n")
