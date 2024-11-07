## IDENTIKITEXT ##

print("\n")
print("## IDENTIKITEXT ##")

# Rules:
#  I.   contiene soltanto lettere
#  II.  contiene soltanto lettere maiuscole
#  III. contiene soltanto lettere minuscole
#  IV.  contiene soltanto cifre numeriche decimali
#  V.   contiene soltanto lettere e cifre

#  VI.  inizia con una lettera maiuscola
#  VII. termina con un punto

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
