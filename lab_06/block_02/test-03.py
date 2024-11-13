## AERODYNAMIC RESISTANCE ##

print("\n")
print("## AERODYNAMIC RESISTANCE ##")

def main():
  AIR_DENSITY = 1.23 # kg/m^3\
  CAR_SURFACE = 2.5 # m^2
  COEF_REF = 0.2
  velocity_input = input("Please enter car's velocity: ")
  velocity = int(velocity_input)
  force = (1/2) * AIR_DENSITY * (velocity ** 2) * CAR_SURFACE * COEF_REF
  get_values(force, velocity)
  
def get_values(force, velocity):
  power = force * velocity
  horse_power = round(power / 745.7, 2)
  print(f"We need {power}W or {horse_power}Hp to superate resistance force")

main()
print("\n")
