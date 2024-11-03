## THE DRUNKEN WALK ##
import random

print("\n")
print("## THE DRUNKEN WALK ##")

print("We will simulate a drunken person, who choose between 4 cardinals directions in each cross")
print("We will use (x, y) coordinates to show how it change\n")

print("But first of all, how many choices will have our drunken friend?")
steps = int(
  input("Enter a number of steps: ")
)

x = 0
y = 0

for index in range(steps):
  x += random.choice([-1, 1])
  y += random.choice([-1, 1])

print(f"Our drunken friend init his adventure at:\n(0, 0)")
print(f"After {steps} of questionable decisions, he arrived to:\n({x}, {y})")

print("\n")
