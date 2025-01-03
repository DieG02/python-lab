## JOIN WORDS ##
# NOTE:
# Absolutely we can use list, but in this case,
# I was not interested in displaying the words in order as it is not a requirement

print("\n")
print("## JOIN WORDS ##")
print("")

def main():
  print("We will play a game, where the new word must to be the last 2 characteres of the last one")
  last = ""
  dicc = set()
  stop = False 
  turn = 0
  
  while not stop:
    player = (turn % 2) + 1
    entry = input(f"Player {player} your turn! Enter a word that begins with `{last[-2:]}`: ")
    # Check:
    # - Not repeated words
    # - Last 2 characters equals to first 2 characters
    # - Alphabetic characters only!
    validation = entry not in dicc and last[-2:] == entry[:2] and entry.isalpha()
    
    if last == "" or validation:
      last = entry
      dicc.add(entry)
      turn += 1
      print(f"Current words are: {dicc}\n")
    else:
      stop = False
      print(f"Player {player} loses!")

main()
print("\n")
