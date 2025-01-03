## WORKING WITH LISTS ##

print("\n")
print("## WORKING WITH LISTS ##")
print("")

def main():
  values = input("Enter integer values, use `:` as separator: ")
  arr = values.split(':')
  # arr = ["24", "19", "0", "86", "32", "7"]
  filter_1(arr)
  filter_2(arr)
  filter_3(arr)

def filter_1(arr: list[str]) -> list:
  data = arr.copy()
  min_val = min(data)
  data.remove(min_val)
  max_val = max(data)
  data.remove(max_val)
  print(":".join(data))

def filter_2(arr: list[str]) -> list:
  data = arr.copy()
  data = filter(lambda n: int(n) % 2 == 0, data)
  print(":".join(data))
  
  
def filter_3(arr: list[str]) -> list:
  data = arr.copy()
  data = filter(lambda n: len(n) == 2, data)
  print(":".join(data))
  
main()
print("\n")
