## LEARN HOW TO STOP ##

print("\n")
print("## LEARN HOW TO STOP ##")

pi = 3.14159265358979323846264338327950228841971

print("Value of π/4:", round(pi / 4, 6))

acc = 0
change = True
for i in range(100):
  if i%2 == 1:
    val = 1/i if change else (-1)/i
    acc +=val
    change = not change
print("Value of aprox:", round(acc, 6))

x = 1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11 + 1/13
print("Value with only 6 first elements:",round(x, 6))