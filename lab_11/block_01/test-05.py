## SPARSE ARRAY SUM ##

print("\n")
print("## SPARSE ARRAY SUM ##")
print("")

def main():
  # a = list([0, 0, 3, 3, 5, 0, 1, 2, 0])
  a = dict({ "2": 3, "3": 3, "4": 5, "6": 1, "7": 2 })
  # b = list([0, 0, 8, 1, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 7])
  b = dict({ "2": 8, "3": 1, "8": 9, "14": 7})
  
  # c = list([0, 0, 11, 4, 5, 0, 1, 2, 9, 0, 0, 0, 0, 0, 7])
  result = sparse_array_sum(a, b)
  print(result)
  
def sparse_array_sum(a: dict[str, int], b: dict[str, int]) -> dict:
  sum = dict()
  keys = set(a.keys()).union(b.keys())
  
  for key in keys:
    if key in a and key in b:
      sum[key] = int(a[key]) + int(b[key])
    elif key in a:
      sum[key] = int(a[key])
    elif key in b:
      sum[key] = int(b[key])
  
  return sum

main()
print("\n")
