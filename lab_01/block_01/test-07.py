## BACK TO THE ROOTS ##
import math

print("\n")
print("## BACK TO THE ROOTS ##")

number = int(input("Enter a N natural number: "))
if(number <= 0):
  print("Invalid input, we expect a natural number...")
  exit()
  
acc = number/2
for i in range(1, 5):
  acc = (1/2) * (acc + number/acc)
  
acc_10 = number/2
for i in range(1, 10):
  acc_10 = (1/2) * (acc_10 + number/acc_10)


print("\nWe will try to calculate the root with `Babilonese Method`\n")
print(f"So the real square of {number} is: {math.sqrt(number)}\n")
print(f"If we only use 5 steps we get: {acc}\n")
print(f"If we only use 10 steps we get: {acc_10}\n")
print("So we can conclude, with more iterations more similar is the result")
  