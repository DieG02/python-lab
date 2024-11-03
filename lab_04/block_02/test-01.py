## THE GAME OF NIM ##
import random
import time

print("\n")
print("## THE GAME OF NIM ##")

print("Two players must take it in turns to take a minimum of one and a maximum of half of the marbles available")
print("The player who takes the last marble loses the game")

# total = random.randint(1, 10)
total = 10
start = random.choice([0, 1]) # 0 = PC / 1 = USER
mode = input("Do you wanna use vs. AI?:\n1 = YES / 0 = NO\n")

def loading_prompt (strg, sleep=0.5, character="."):
  tail = ""
  for i in range(3):
    tail += character
    # NOTE: This is how we can `update` a print in the same line
    # \r `carriage return` & `end = ""` 
    print(f"\r{strg}{tail}", end="")
    time.sleep(sleep)
  print("")
  
def valid_movements (movement, subtotal):
  global total # For access to `total` from global enviroment
  if (movement > 0) & (movement <= int(subtotal/2)):
    total -= movement
    return True
  else: 
    return False


if mode == "1":
  loading_prompt("Enabling AI, this could take a while", 1)
  print("\n--- Smart AI Mode Enabled ---\n")


else:
  print("\n--- Fooly Mode Enabled ---\n")
  flag = start
  
  print(f"{'PC' if flag == 0 else 'USER'} starts")
  while total > 1:
    print("\nSubtotal is", total)
    if flag == 0:
      pc_move = random.randint(1, int(total/2)) # 4
      loading_prompt(f"PCs move: {pc_move}", 0.5, "")
      if valid_movements(pc_move, total): 
        flag = 1
    else: 
      user_move = int(input("Provide a number: ")) # 4
      if valid_movements(user_move, total): 
        flag = 0
        
  print(f"\n{'PC' if flag == 0 else 'USER'} loses")
      


print("\n")
