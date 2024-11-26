## LOCAL MAX ##
import math

print("\n")
print("## LOCAL MAX ##")

def main():
  arr = generate_list()
  get_local_max(arr)
  
def generate_list():
  arr = list()
  while True:
    num_input = input("Enter a number: ")
    if(num_input == ""): break
    try:
      num = int(num_input)
      arr.append(num)
    except ValueError:
      print("Please enter a valid number.\n")
      continue
  return arr
  
def get_local_max(a):
  arr = [2, 3, 5, 6, 7, 3, 2, 1, 1, 3, 5, 6, 11, 2, 3, 1]
  length = len(arr)
  locale_max = []
  locale_index = []
  result = []
  acc = float('inf')
  
  for i in range(1, length-1):
    if arr[i-1] < arr[i] and arr[i] > arr[i+1]:
      locale_max.append(arr[i])
      locale_index.append(i)
  
  if len(locale_max) == 0:
    print("There is not local max values")
    return None
  
  for i in range(len(locale_index) - 1):
    a = abs(locale_index[i] - locale_index[i+1])
    if acc > a:
      acc = a
      result = [locale_index[i], locale_index[i + 1]]
  
  print(f"The array generated is {arr} and the max found are {locale_max}")
  print(f"The closest couple of local max is located at {result}")
  return locale_max



main()
print("\n")
