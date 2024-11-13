## ROMAN NUMBERS ##
import re
from functools import reduce
# NOTE: How to use `reduce` in Python:
# result = reduce(function, iterable, [initializer])
# NOTE: When we use `lambda`?
# We use `lambda` for `inline functions`, for ex. as callback functions in `Typescript`

# So this `lambda x, y: x + y` is equal to this:
# def add(x, y): 
#   return x + y
# reduce(add, list_numbers)


print("\n")
print("## ROMAN NUMBERS ##")

digits = { "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000 }

def is_valid_roman(roman):
  # Espressione regolare per numeri romani validi
  pattern = r"^(M{0,3})(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"
  return bool(re.match(pattern, roman))

def roman(string):
  if not is_valid_roman(string):
    return print(f"{string} is not a valid input")
  
  numbers = []; result = 0; min = digits["M"] # Max value valid
  
  for i, ch in enumerate(list(string)):
    # Get int value
    value = digits[ch]
    
    # Update `min` or change sign in the previous value & add to `numbers`
    if(min >= value):
      min = value
    else:
      numbers[i-1] = numbers[i-1] * (-1)
    numbers.append(value)      
    
    # We use the module `functools` for a fast sum of integers
    result = reduce(lambda x, y: x + y, numbers)
  print(result)

roman("MCMLXXVIII")
roman("MDCCCXLIV")
roman("MMII")
roman("MLXXVI")
roman("MMMCDLXXXIII")
print("\n")
