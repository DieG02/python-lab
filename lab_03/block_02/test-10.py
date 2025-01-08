## ESCAPE ON HALLEY'S COMET ##

print("\n")
print("## ESCAPE ON HALLEY'S COMET ##")

G = 6.67e-11 # Gravitational constant in N·m^2/kg^2
def escape_velocity():
  
  print("Check if a person jumping with a given speed can return to Halley's comet surface")
  jump_speed_kmh = input("Enter the jump speed (in km/h): ")
  jump_speed_ms = float(jump_speed_kmh) * (1000 / 3600)
  radius_comet = 9.4 / 2 * 1000
  mass_comet = 2.2e14
  
  v_escape = (2 * G * mass_comet / radius_comet) ** 0.5
  
  # Compare jump speed with escape velocity
  if jump_speed_ms < v_escape:
    print("\nThe person will return to the comet's surface")
  else:
    # If jump speed exceeds escape velocity, calculate the required mass to make them return
    new_mass = (jump_speed_ms ** 2 * radius_comet) / (2 * G)
    mass_increase = new_mass - mass_comet
    print("\nThe person will not return to the comet's surface")
    print(f"The comet's mass needs to increase by {mass_increase:.2e} kg to make this possible")
    
escape_velocity()
print("\n")
