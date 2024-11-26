## SORT A RANDOM LIST##
import random

print("\n")
print("## SORT A RANDOM LIST##")

def main():
  random_list = []
  for _ in range(20):
    random_list.append(random.randint(0, 99))
  print(random_list)
  sortList(random_list)

def sortList(list):
  list.sort()
  print(list)
  
main()
print("\n")
