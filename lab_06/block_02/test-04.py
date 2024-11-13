## ELECTRIC EDGE ##
import math
pi = math.pi

print("\n")
print("## ELECTRIC EDGE ##")

def main():
  copper_res = round(copper_wire_resistance(3, 90), 4)
  aluminum_res = round(aluminim_wire_resistance(3, 90), 4)
  print(f"Copper resistance: {copper_res}")
  print(f"Aluminum resistance: {aluminum_res}")

def diameter(wire_guage):
  return 0.127 * 92 ** ((36 - wire_guage) / 39)

def copper_wire_resistance(length, wire_guage):
  COPPER_RES = 1.678 * (10**(-8))
  d = diameter(wire_guage)
  return (4 * COPPER_RES * length) / (pi * (d**2))

def aluminim_wire_resistance(length, wire_guage):
  ALUMINUM_RES = 2.82 * (10**(-8))
  d = diameter(wire_guage)
  return (4 * ALUMINUM_RES * length) /( pi * (d**2))

main()
print("\n")
