## RANDOM LIST ##
import random

print("\n")
print("## RANDOM LIST ##")

def main():
  random_list = list([])
  for _ in range(10):
    n = random.randrange(1, 100)
    random_list.append(n)
    
  print(random_list[:: 2]) # Even indexes
  print([num for num in random_list if num % 2 == 0]) # Even values
  print(random_list[:: -1]) # Reverse list
  print([random_list[:1][0], random_list[-1:][0]]) # First and last values

main()
print("\n")
