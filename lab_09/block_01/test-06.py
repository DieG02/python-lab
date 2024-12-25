## WORKING WITH LISTS ##

print("\n")
print("## WORKING WITH LISTS ##")
print("")

def main():
  # values = input("Enter integer values, use `:` as separator: ")
  # arr = values.split(':')
  arr = ["24", "19", "0", "86", "32", "7"]
  filter_1(arr)
  filter_2(arr)
  filter_3(arr)

def filter_1(arr: list[str]) -> list:
  data = arr.copy()
  min = data[0]; min_i = 0
  max = data[0]; max_i = 0
  
  # Find the min & max element with their index, keeping the original positions
  for i in range(len(data) - 1):
    if int(min) > int(data[i]):
      min = data[i]
      min_i = i
    if int(max) < int(data[i]):
      max = data[i]
      max_i = i
      
  # Delete first the element with higher index to avoid cut in the middle
  data.pop(min_i if min_i > max_i else max_i)
  data.pop(min_i if min_i < max_i else max_i)
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
