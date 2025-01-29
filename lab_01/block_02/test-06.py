## BANK'S INTEREST ##

print("\n")
print("## BANK'S INTEREST ##")
print("")
  
# After each year, we update `initial_amount` value
initial_amount = 1000
interests = 0.05

initial_amount = initial_amount * (1 + interests)
print("1º year: ", initial_amount)

initial_amount = initial_amount * (1 + interests)
print("2º year: ", initial_amount)

initial_amount = initial_amount * (1 + interests)
print("3º year: ", initial_amount)


print("\n")