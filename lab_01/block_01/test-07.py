## BACK TO THE ROOTS ##
import math

print("\n")
print("## BACK TO THE ROOTS ##")

square_input = input("Enter a N natural number: ")
number = int(square_input)

if(number <= 0):
  print("Don't you know what is a natural number?")
  exit()
  
acc = number/2
for i in range(1, 5):
  acc = (1/2) * (acc + number/acc)
  
acc_10 = number/2
for i in range(1, 10):
  acc_10 = (1/2) * (acc_10 + number/acc_10)

print("We will try to calculate the root with `Babilonese Method`\n")
print("So the real square of", number, "is:")
print(math.sqrt(number), "\n")
print("And with our `Babilonese Method` is:")
print(acc, "for 5 steps \n")
print(acc_10, "for 10 steps \n")
  