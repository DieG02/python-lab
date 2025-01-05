## PLAYFAIR CIPHER ##
import os
# NOTE: This exercise could be improved so far
# At this point, decrypt function doesn't work 100% as expected due to problems with data loss.
# So, the current behaviour is to have errors with odd words
# Also, the PLAYFAIR CIPHER doesn't works as I thought,
# Because they are just all characters together without spaces between, and points, etc

print("\n")
print("## PLAYFAIR CIPHER ##")
print("")

ALPHABET = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
KEY_DECODE = "ZEBRA"
# TESTING = "He felt his smile slide away, then it's gone!"
PROCESS = {
  "E": "ENCRYPT",
  "D": "DECRYPT"
}

def main():
  print("Welcome to this encrypt/decrypt manager")
  type = input("Enter E(Encrypt) or D(decrypt): ").upper()
  filename = input(f"Choose a file from `/input` folder to be {'encripted' if type == 'E' else 'decrypted'}: ")
  key = input(f"Now enter the key to use for {'encript' if type == 'E' else 'decrypt'}: ")
  secret = get_secret(key if type == "E" else KEY_DECODE) # Use default key for case_02
  system = get_matrix(secret)

  print("This is the Playfair Scheme to use:\n")
  for i in range(5):
    print(system[i])
  print("")
  
  base = os.path.join("lab_10/block_02", "utils", "test-03")

  with open(os.path.join(base, "input", filename), "r") as file:
    template = list()
    for raw_line in file:
      row = process(raw_line.strip(), PROCESS[type], system)
      template.append(f"{row}\n")
      
  os.makedirs(os.path.join(base, "output"), exist_ok=True)
  with open(os.path.join(base, "output", filename), "w") as file:
    file.write("".join(template))


def get_secret(word: str) -> str:
  word = word.upper().strip().replace("J", "I")
  aux = set(word)
  key = []
  for _, ch in enumerate(word):
    if ch in aux:
      key.append(ch)
      aux.remove(ch)
  return "".join(key)
  
def get_matrix(key: str) -> list[list]:
  alphabet = ALPHABET.copy()
  alphabet.remove("J")
  for i in range(len(key)):
    alphabet.remove(key[i])
    
  system = list(key) + alphabet
  matrix = list()
  for i in range(5):
    matrix.append(system[i*5:(i+1)*5])
  return matrix
      
def get_format(word: str, aux: str) -> dict:
  current = list() # Convert to list
  restore = list() # Save temporaly index for restore after the encrypt
  if not word.isalpha():
    # Clean here as you want
    for index, ch in enumerate(word):
      # i t ' s
      if ch.isalpha():
        current.append(ch) # ["i", "t", "s"]
      else:
        restore.append(index) # ["'"]
  else:
    current = list(word)
    
  if len(current)%2 != 0:
    current.append(aux)
    restore.append(-1)
    
  return {
    "current": current,
    "restore": restore
  }

# NOTE: function `process` has problems with data loss,
# because when adding information related to the characters and then deleting it, 
# as in the odd ones, the information of the missing part is lost, 
# making it impossible to recover with accuracy, 
# of course it is readable but not 100% as it should be.
def process(text: str, type: str, system: list[list]) -> str:
  # He felt his smile slide away, then it's gone!
  # ["He", "felt", "his", "smile", "slide", "awAy,", "then", "it's", "gone!"]
  words = text.strip().split(" ") # Remove this line
  # We cannot define if a `word` is even or not, so we manage a virtual `word` in realtime
  aux = system[4][4]
  template = list()
  
  for word in words:
    data = get_format(word, aux)
    restore: list[str] = data['restore']
    current: list[str] = data['current']
    result = list()
    
    for i in range(0, len(current) - 1, 2):
      ch_1, ch_2 = current[i], current[i+1]
      is_lower_1, is_lower_2 = [ch_1 == ch_1.lower(), ch_2 == ch_2.lower()]
      if type == "ENCRYPT":
        [cyp_1, cyp_2] = encrypt(ch_1, ch_2, system)
        result.append(cyp_1.lower() if is_lower_1 else cyp_1)
        result.append(cyp_2.lower() if is_lower_2 else cyp_2)
      elif type == "DECRYPT":
        [cyp_1, cyp_2] = decrypt(ch_1, ch_2, system)  
        print([ch_1, ch_2], [cyp_1, cyp_2])      
        result.append(cyp_1.lower() if is_lower_1 else cyp_1)
        result.append(cyp_2.lower() if is_lower_2 else cyp_2)
      
    if len(restore) > 0:
      # Remove auxiliar character if it's necesary (added to have even words)
      if -1 in restore:
        result.pop()
        restore.remove(-1)
      # Restore punctuation marks and other characters of the original word
      for index in restore:
        result.insert(index, word[index])
        
    template.append("".join(result))
      
  return " ".join(template)
      
def encrypt(ch_1: str, ch_2: str, system: list[list[str]]) -> list[str]:
  ch_1 = ch_1.upper()
  ch_2 = ch_2.upper()
  
  # If ther are equals, don't do anything
  if ch_1 == ch_2:
    return [ch_1, ch_2]
  
  y_1, x_1 = 0, 0
  y_2, x_2 = 4, 4
  for i in range(5):
    if ch_1 in system[i]:
      [y_1, x_1] = [i, system[i].index(ch_1)]
    if ch_2 in system[i]:
      [y_2, x_2] = [i, system[i].index(ch_2)]
      
  if x_1 == x_2:
    return [system[y_2][x_1], system[y_1][x_2]]
  else:
    return [system[y_1][x_2], system[y_2][x_1]]
    

def decrypt(ch_1: str, ch_2: str, system: list[list[str]]) -> list[str]:
  ch_1 = ch_1.upper()
  ch_2 = ch_2.upper()
  
  # If ther are equals, don't do anything
  if ch_1 == ch_2:
    return [ch_1, ch_2]
  
  y_1, x_1 = 0, 0
  y_2, x_2 = 4, 4
  for i in range(5):
    if ch_1 in system[i]:
      [y_1, x_1] = [i, system[i].index(ch_1)]
    if ch_2 in system[i]:
      [y_2, x_2] = [i, system[i].index(ch_2)]
      
  if x_1 == x_2:
    return [system[y_2][x_1], system[y_1][x_2]]
  else:
    return [system[y_1][x_2], system[y_2][x_1]]

main()
print("\n")
