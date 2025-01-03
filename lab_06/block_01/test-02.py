## WORDS COUNTER ##

print("\n")
print("## WORDS COUNTER ##")

def count_words(string):
  count = len(string.split(' '))
  print(count)
  return count

count_words('This is a looong sentence')
print("\n")
