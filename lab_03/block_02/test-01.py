## TRENDS ##

print("\n")
print("## TRENDS ##")

def has_order():
  print("This function allows to identify if 3 numbers are ordered or not")
  entry = input("Enter a 3 numbers sequence: ")
  sequence = list(entry.split(" "))
  
  print("")
  # Wich means numbers repeated, it's not ordered extrictly
  if len(set(sequence)) != len(sequence):
    print("neither")
    
  # If we ordered and it's still equal to the begging
  elif sequence == sorted(sequence):
    print("increasing")
    
  # We can ordered in the oppositive way but no matters
  else:
    print("decreasing")
  
  return None

has_order()
print("\n")
