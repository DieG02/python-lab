## FACTORISATION OF INTEGERS ##

print("\n")
print("## FACTORISATION OF INTEGERS ##")

print("For this test, we will factor an integer, then...")
number = int(
  input("Please provide an integer number: ")
)

optimized = int(round((number + 1)/2))
factors = list()

for factor in range(1, optimized):
  if number%factor == 0:
    factors.append(factor)

factors.append(number)
print(f"All the factors of {number} are:\n {factors}")
print("\n")
