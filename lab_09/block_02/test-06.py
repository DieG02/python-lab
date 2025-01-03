## FLOOD MAPPING ##
import random

# NOTE: This exercise is composed of two parts:
# 1) Build a function that receives an array of heights (list[list[int]) of NxN and a water level, and displays the flooded parts.
# 2) Load random values into the `heights` matrix, take the max/min, and make a `map` within 10 values.

print("\n")
print("## FLOOD MAPPING ##")
print("")

def generate(m, n):
  # Generate a matrix with random values between 0 and 99
  return [[int(random.random() * 150) for _ in range(n)] for _ in range(m)]

def printf(table):
  print("")
  for _, arr in enumerate(table):
    row = ""
    for _, el in enumerate(arr):
      row += f"{str(el):<4}"
    print(row)

def main():
  heights = generate(10, 10)
  min_arr = list()
  max_arr = list()
  for _, arr in enumerate(heights):
    min_arr.append(min(arr))
    max_arr.append(max(arr))
  # Get step in this matrix, based on min/max values
  step = int((max(max_arr) - min(min_arr)) / 10)
  printf(heights)
  print(f"\nStep between max = {max(max_arr)} and min = {min(min_arr)} is {step}\n")
  display(heights, step)

def flood_map(heights: list[list[int]], water_level: int) -> None:
  """
  Shows the flooded or dry areas of an altitude map
  :param `heights`: matrix of the heights `NxN`
  :param `water_level`: the current level of water
  :return: display areas at a specific water level
  """
  
  print("")
  for _, arr in enumerate(heights):
    row = list()
    for _, el in enumerate(arr):
      if el <= water_level:
        row.append("*")
      else:
        row.append(" ")
    print(" ".join(row))
  print("\n")

def display(heights: list[list[int]], step) -> None:
  for i in range(10):
    print(f"Water level: {step * i}")
    flood_map(heights, step * i)

main()
print("\n")
