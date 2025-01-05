## ENCODE AND DECODE ##
#  NOTE: `encode` & `decode` are substantially the same, 
#  only the way they read the dictionaries changes.
#   index = ALPHABET.index(ch)      =>    index = system.index(ch)
#   encoded_row += system[index]    =>    decoded_row += ALPHABET[index]
import os

print("\n")
print("## ENCODE AND DECODE ##")
print("")

ALPHABET = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
KEY_DECODE = "MURCIELAGO"

def main():
  base = os.path.join("lab_10", "block_02", "utils", "test-01")
  filename = input("Enter the name of a file: ")
  process = input("Do you want to E(encode) or D(decode) this file?: ") 
  key_input = input("Enter your secret key (word): ")
  key = clean_key(key_input)
  
  if process.upper() == "E":
    encode(base, filename, key)
  elif process.upper() == "D":
    # Ignore key entry for testing porpuses
    decode(base, filename, KEY_DECODE)
  else:
    print("Invalid option!")
     
     
def clean_key(word: str) -> str:
  # We can recive everything as key, so we must to clean it before
  # NOTE: This function caused a bug with `Copernico` because "C" != "c"
  word = word.upper()
  aux = set(word)
  key = str()
  for _, ch in enumerate(word):
    if ch in aux:
      key += ch
      aux.remove(ch)
  return key.upper()

def get_system(key: str) -> str:
  """\
  Generate a new alphabet with the clean key at the begging
  """
  system = ALPHABET.copy()
  print(f"Key: {key}")
  # Remove repeated letters from the original alphabet in order to avoid problems
  for _, letter in enumerate(key):
    system.remove(letter)
  system.reverse()
  system = list(key) + system
  print(f"\n{ALPHABET}\n{system}\n")
  return system


def encode(url: str, filename: str, key: str) -> None:
  system = get_system(key)
  with open(os.path.join(url, "input", filename), "r") as file:
    template = list()
    for _, row in enumerate(file):
      encoded_row = ""
      for _, ch in enumerate(row.strip()):
        # Different behaviours if they are UPPERCASE or LOWERCASE
        if ch.upper() == ch and ch.isalpha():
          # If `ch` is UPPERCASE, let it by default 
          index = ALPHABET.index(ch)
          encoded_row += system[index]
          
        elif ch.lower() == ch and ch.isalpha():
          # If `ch` is LOWERCASE, seek the UPERCASE value and then return to the original
          index = ALPHABET.index(ch.upper())
          encoded_row += system[index].lower()
          
        else:
          # If isn't a character, just add itselft
          encoded_row += ch
    
      template.append(f"{encoded_row}\n")
      
  with open(os.path.join(url, "output", filename), "w") as file:
    file.write("".join(template))


def decode(url: str, filename: str, key: str) -> None:
  system = get_system(key)
  with open(os.path.join(url, "input", filename), "r") as file:
    template = list()
    for _, row in enumerate(file):
      decoded_row = ""
      for _, ch in enumerate(row.strip()):
        # Different behaviours if they are UPPERCASE or LOWERCASE
        if ch.upper() == ch and ch.isalpha():
          # If `ch` is UPPERCASE, let it by default 
          index = system.index(ch)
          decoded_row += ALPHABET[index]
          
        elif ch.lower() == ch and ch.isalpha():
          # If `ch` is LOWERCASE, seek the UPERCASE value and then return to the original
          index = system.index(ch.upper())
          decoded_row += ALPHABET[index].lower()
          
        else:
          # If isn't a character, just add itselft
          decoded_row += ch
    
      template.append(f"{decoded_row}\n")
      
  with open(os.path.join(url, "output", filename), "w") as file:
    file.write("".join(template))

main()
print("\n")
