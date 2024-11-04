## WORD IN PARTS ##

print("\n")
print("## WORD IN PARTS ##")

def decompose_word():
  word = input("Write just a word: ")
  length = len(word)
  for i in range(length):
    limit = length - i
    j = 0
    while limit > 0:
      val = word[j:j+i+1]
      print(val)
      j += 1
      limit -= 1
      
decompose_word()
print("\n")
