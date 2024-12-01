## CORRECTION OF THE AVERAGE ##
import random

print("\n")
print("## CORRECTION OF THE AVERAGE ##")

def main():
  result = [21, 94, 69, 24, 40, 18, 11, 25, 87, 79, 85, 66, 26, 0, 74, 62, 14, 14, 51, 81]
  length = len(result) - 1
  
  # This is optional, but I decided to include it bc it's clearer to see what the function does
  result.sort()
  print(f"Original list:\n{result}")
  
  for i in range(1, len(result) - 1):
    result[i] = int((result[i-1] + result[i] + result[i+1]) / 3)
  result[0] = int((result[0] + result[1]) / 2)
  result[length] = int((result[length] + result[length-1]) / 2)
  print(f"Correction of the average values, new list:\n{result}")

def reset():
  pass

main()
print("\n")
