## SUM WITHOUT SMALLEST ##
# NOTE: list.pop(index = 0) => array.shift()
from functools import reduce

print("\n")
print("## SUM WITHOUT SMALLEST ##")

def main():
  v = [31, 7, 5, 20, 5, 34, 3]
  print(f"The original list is {v}")
  sum = sum_without_smallest(v)
  print(f"The sum of all values from the list without the smallest is {sum}")

def sum_without_smallest(v):
  v.sort()
  v.pop(0)
  return reduce(lambda x, y: x + y, v)

main()
print("\n")
