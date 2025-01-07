## GENETIC CODE ##
import os

print("\n")
print("## GENETIC CODE ##")
print("")

def main():
  print("Welcome to our Biology Bot")
  print("We will work with RNA, so...")
  # code = input("Enter a RNA sequence, we will do the rest: ")
  code: str = "GUAUGCACGUGACUUUCCUCAUGAGCUGAU"

  print("\n")
  
  table = dict()
  trigger = dict()
  
  filename = os.path.join("lab_11/block_02", "utils", "test-02", "genetic_code.csv")
  with open(filename, "r") as file: 
    for line in file:
      [name, *items] = line.strip().split("\xa0")
      if name == "start" or name == "stop":
        trigger[name] = tuple(items[0][2:].split(", "))
      else:
        result = items[0].split('"')
        result = "".join(result).split(',')
        result = "".join(result).split(' ')
        for key in result:
          table[key] = name
  
  sequence = start(code, trigger)
  splitted = []
  for i in range(3, len(sequence), 3):
    splitted.append(sequence[i-3:i])
  
  if len(sequence) == 0:
    print("Start RNA not found!")
    return None
  
  stop = False
  result = ""
  for rna in splitted:
    if rna not in table:
      stop = True
      break
    result += table[rna]
    
  if not stop:
    print("Stop RNA not found!")
    return None
  print(result)
     
  
def start(code: str, trigger: dict[str, tuple]) -> str:
  init = []
  for start in trigger["start"]:
    if code.find(start) != -1:
      init.append(code.find(start))
  index = min(init, default=-1)
  if index == -1:
    return ""
  else:
    return code[index:]

main()
print("\n")
