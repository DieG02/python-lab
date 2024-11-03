## RANDOM NUM GENERATOR ##

print("\n")
print("## RANDOM NUM GENERATOR ##")

print("Today we will try to create a random num generator")
print("We will use the following formula: r_new = (a x r_old + b) % m")
print("Also, we use all default values, but we can choose the nº of iterations")

loop = int(input("How many iterations do you want?: "))
a = 32310901; b = 1729; m = 2**24

res_new = 1
for index in range(loop):
  res_new = (a * res_new + b) % m
  
print("The random number generated is:", res_new)

print("\n")
