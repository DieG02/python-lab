## DICE THROWING ##
# NOTE: `inline` loop with for-in
import random

print("\n")
print("## DICE THROWING ##")

def main():
  play()

def play():
  # Create a random list with 20 positions
  queue = [random.randint(1, 6) for _ in range(20)]
  print(f"\n{queue}\n")
  
  # 
  max = { "init": 0, "length": 1 }
  flag = None
  length = 0 # Length of the succession
  index = 0 # Position of the init of the succession
  
  for i, el in enumerate(queue):
    if el == flag:
      # if equals, increment max.length
      max["length"] += 1
    else:
      # if not, reset max counter
      max["init"] = i
      max["length"] = 1
      flag = el
  
    # Get the correct initial position (not current position)
    if max["length"] > length:
      length = max["length"]
      index = i - (length - 1)
    
  print(f"{'Longest succesion':<24}{length}\n{'Value repeated':<24}{queue[index]}\n{'Inits at position':<24}{index}")
      
main()
print("\n")
