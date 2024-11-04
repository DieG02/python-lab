## REVERSE WORD ##

# NOTE: 
# This exercise was really anoying
# `split`, `reverse`, `join` doesn't work as expected
# Pay attenttion to these details

print("\n")
print("## REVERSE WORD ##")

def reverse_word():
  word = input("Enter a word: ")
  arr = list(word)
  arr_upper = list() 
  
  for index, ch in enumerate(word):
    lower = word.lower()
    if lower[index] != ch:
      arr_upper.append(ch)
    
  arr.reverse()
  arr_upper.reverse()
  
  print(''.join(arr))
  print(''.join(arr_upper))

reverse_word()
  
print("\n")
