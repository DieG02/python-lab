## IDENTIKITEXT ##

print("\n")
print("## IDENTIKITEXT ##")

# Rules:
#  I. contains only letters
#  II. contains only uppercase letters
#  III. contains only lowercase letters
#  IV. contains only decimal numeric digits
#  V. contains only letters and digits

#  VI. begins with an uppercase letter
#  VII. ends with a period

def get_phrase():
  print("You provide a word and if it is ok with one option, we tell you wich is more accurate")
  word = input("Enter a word: ")

  if word.isalpha():
    print("Your text has only alphanumeric characters")
    
  elif word.isalpha():
    if word.isupper():
      print("Your text has only upper case characters")
    elif word.islower():
      print("Your text has only lower case characters")
    else:
      print("Your text has only letters as characters")
      
  elif word.isdecimal():
    print("Your text has only decimal numbers")
    
  elif word[0].islower():
    print("Your text inits with a lower case character")

  elif word[-1] == '.':
    print("Your text ends with a dot")
  else:
    print("There is not category for your text")

  
get_phrase()
print("\n")
