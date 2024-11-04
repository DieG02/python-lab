## INTEGERS NUMBER ##

print("\n")
print("## INTEGERS NUMBER ##")

def integer_numbers():
  acc = " "
  elements = []
  odd = [] # 1, 3, 5
  even = [] # 2, 4, 6
  while (acc != 'e') or (acc != ""):
    acc = input("\rEnter a number (or 'e' for exit): ")
    if (acc != "e") and (acc != ""):
      acc = int(acc)
      if acc % 2 == 0:
        even.append(acc)
      else:
        odd.append(acc)
      elements.append(acc)
    else:
      acc = ""
      break
  min_val = min(elements)
  max_val = max(elements)
  sum_values = sum(elements)
  
  print("")
  print(f"{'Sum value:':<15} {sum_values}")
  print(f"{'Min value:':<15} {min_val}\n{'Max value:':<15} {max_val}")
  print(f"{'Odd Elements:':<15} {odd}\n{'Even Elements:':<15} {even}")
  
integer_numbers()

print("\n")
