## VOWELS COUNTER ##
# NOTE: This is how works some features
# `split`: str.split(' ') -> only with some valid character -> return list
# `join`: str.join(arr_to_join) -> inital text is the ch used for join -> return string
# `list`: list(str) -> destructure my string -> return list
# example: list(''.join(text.split(' '))) -> remove empty spaces, join into a single str, then destructure in a list

print("\n")
print("## VOWELS COUNTER ##")

def count_vowels(string):
  split_text = list(string.lower())
  print(split_text)
  total_vowels = 0
  for i, ch in enumerate(['a', 'e', 'i', 'o', 'u']):
    count = split_text.count(ch)
    if count > 0:
      total_vowels += count
      
  print(total_vowels)
  return total_vowels
  
count_vowels('this is some value')
print("\n")
