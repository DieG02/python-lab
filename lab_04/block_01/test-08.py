## REPEATED NUMBERS ##
# NOTE: This was a pretty implementation of `index` handling and `set`

print("\n")
print("## REPEATED NUMBERS ##")

def get_repeat_numbers():
  num = 0; acc = set(); reapeat = set()
  while num != "":
    num = input(f"{'Enter a number:':<20}")
    if num != "":
      if num in acc:
        reapeat.add(num)
      acc.add(num)
      print(f"{'Values registered:':<20}{' '.join(acc)}")
      print(f"{'Values repeated:':<20}{' '.join(reapeat)}")
      print("")
    
get_repeat_numbers()
print("\n")
