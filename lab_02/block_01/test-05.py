## COLOUMB'S LAW ##
import math

print("\n")
print("## COLOUMB'S LAW ##")

print("For this test we'll calculate Electric Force: ")
q_1_input = input("Provide the value of Q1 [C]: ")
q_2_input = input("Provide the value of Q2 [C]: ")
distance_input = input("How long are they? Provide the value in [m]: ")
q_1 = float(q_1_input)
q_2 = float(q_2_input)
distance = float(distance_input)

pi_value = math.pi
epsilon = 8.8541878128 * (10**-12)
force = (q_1 * q_2) / (4 * pi_value * epsilon * (distance**2))

print("Electric Force between Q1 & Q2 to a", distance, "m is:")
print(round(force, 4))
print("")