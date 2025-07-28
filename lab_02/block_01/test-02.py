## RESISTANCE ##

print("\n")
print("## RESISTANCE ##")

print("You have three resistences in a mix-circuit\n")
r_1 = int(input("Please provide the value of R1: "))
r_2 = int(input("Please provide the value of R2: "))
r_3 = int(input("Please provide the value of R3: "))

r_eq = 1 / ((1 / r_2) + (1 / r_3))
r_tot = r_1 + r_eq

print("\nSo if we have R1 / R2//R3, Rt would be:")
print(int(r_tot), "ohms")

print("\n")
