## LIST OF FUNCTIONS ##
# NOTE: This is how we can type a function
# def func_n(array: list[int]) -> None:
import random

print("\n")
print("## LIST OF FUNCTIONS ##")
print("")

def main():
  test = [f"{random.randint(1, 50):<2}" for i in range(10)]
  test = [random.randint(1, 50) for i in range(10)]
  # test = [14, 16, 9, 1, 14, 41, 5, 32, 47, 18]
  print("input_", test, "\n")
  func_1(test.copy())
  func_2(test.copy())
  func_3(test.copy())
  func_4(test.copy())
  func_5(test.copy())
  func_6(test.copy())
  func_7(test.copy())
  func_8(test.copy())
  func_9(test.copy())
  func_10(test.copy())
  
def func_1(arr: list[int]) -> list:
  acc = arr[0]
  arr[0] = arr[-1]
  arr[-1] = acc
  print("func_1", arr, "\n")
  return arr
  
def func_2(arr: list[int]) -> list:
  acc = arr.pop()
  arr.insert(0, acc)
  print("func_2", arr, "\n")
  return arr

def func_3(arr: list[int]) -> list:
  for i in range(len(arr)):
    if i%2 == 0:
      arr[i] = 0
  print("func_3", arr, "\n")
  return arr

def func_4(arr: list[int]) -> list:
  acc = list([arr[0]])
  for i in range(1, len(arr) - 1):
    if arr[i-1] >= arr[i+1]:
      acc.append(arr[i-1])
    else:
      acc.append(arr[i+1])
  acc.append(arr[-1])
  print("func_4", acc, "\n")
  return arr

def func_5(arr: list[int]) -> list:
  length = len(arr)
  i = int(length / 2)
  if length % 2 == 0:
    arr = arr[:i-1] + arr[i+1:]
  else:
    arr = arr[:i] + arr[i+1:]
  print("func_5", arr, "\n")
  return arr

def func_6(arr: list[int]) -> list:
  even, odd = [], []
  for _, n in enumerate(arr):
    if n%2 == 0:
      even.append(n)
    else:
      odd.append(n)
  arr = even + odd
  print("func_6", arr, "\n")
  return arr

def func_7(arr: list[int]) -> list:
  filtered = list()
  for _, el in enumerate(arr):
    if el not in filtered: 
      filtered.append(el) 
  filtered.sort()
  print("func_7", filtered[-2], "\n")
  return arr

def func_8(arr: list[int]) -> list:
  if arr == arr.sort():
    print("func_7", "True", "\n")
    return True
  else:
    print("func_7", "False", "\n")
    return False

def func_9(arr: list[int]) -> list:
  for i in range(1, len(arr)):
    if arr[i-1] == arr[i]:
      print("func_7", "True", "\n")
      return True
  print("func_7", "False", "\n")
  return False

def func_10(arr: list[int]) -> list:
  filtered = list()
  for _, el in enumerate(arr):
    if el not in filtered: 
      filtered.append(el) 
  if len(filtered) != len(arr):
    print("func_7", "True", "\n")
    return True
  else:
    print("func_7", "False", "\n")
    return False
    

main()
print("\n")
