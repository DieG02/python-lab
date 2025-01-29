import math
## LEARN HOW TO STOP ##

print("\n")
print("## LEARN HOW TO STOP ##")

pi = math.pi

print("")
print("Value of π/4:", round(pi / 4, 6))

# We use `reverse` to get a positive/negative sequence
reverse = True
acc = 0

for i in range(100):
  if i%2 == 1:
    val = 1/i if reverse else (-1)/i
    acc += val
    reverse = not reverse
print("Value of aprox:", round(acc, 6))

x = 1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11 + 1/13
print("Value with only 6 first elements:", round(x, 6))