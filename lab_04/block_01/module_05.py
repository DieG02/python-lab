# NOTE
# We cannot use modules named like `test-05`
# The correct name is with `underscore`, so it'd be `test_05`
# I don't want to create an script to change all files, so I've created this one
# It's the same sh*t

def is_prime_number(num):
  index = 1
  arr = []
  
  while index <= num:
    if num % index == 0:
      arr.append(index)
    index += 1
    
  return False if len(arr) > 2 else True