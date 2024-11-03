## RESISTANCE ##

print("\n")
print("## RESISTANCE ##")

print("You have three resistences in a mix-circuit\n")
r1_input = input("Please provide the value of R1: ")
r2_input = input("Please provide the value of R2: ")
r3_input = input("Please provide the value of R3: ")

r_1 = int(r1_input)
r_2 = int(r2_input)
r_3 = int(r3_input)

r_eq = 1 / ((1 / r_2) + (1 / r_3))
r_tot = r_1 + r_eq

print("So if we have R1 / R2//R3, Rtotal would be:")
print(int(r_tot), "ohms")

print("\n")
