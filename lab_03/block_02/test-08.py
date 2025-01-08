## GROCERY VOUCHERS ##
# NOTE: We use `tuple` and `dict`, also we introduce `float('inf')`

print("\n")
print("## GROCERY VOUCHERS ##")

def get_discount():
  print("Free money for groceries! Let's calculate it.")
  print("Find out how much you can save on your next grocery trip.")
  value_input = input("How much are you spent today?: €")
  value = int(value_input)
  
  # This structure allows to get the correct discount easily
  max_value = float('inf')
  breakpoint = dict({
    (0, 10): 0,
    (10, 60): 0.8,
    (60, 150): 0.10,
    (150, 210): 0.12,
    (210, max_value): 0.14,
  })
  
  for (min, max) in breakpoint:
    if value >= 10 and value < max:
      print(f"\nYour discount is €{value * breakpoint[(min, max)]}")
      return
  
  print(f"\nAs you only spent €{value}, we cannot offer a discount yet")
  return
  
get_discount()
print("\n")
