## PREDATORS AND PREY ##

print("\n")
print("## PREDATORS AND PREY ##")

print("We gonna play to be Darwin and how predators & prey are related in nature")
# A. the growth rate of prey;
# B. the rate of destruction of prey by predators
# C. the rate of predator mortality;
# D. the rate of predator increase through prey consumption.
print("Please provide the following inputs: ")
growth_prey_rate = float(input("- The growth rate of prey: "))
destruction_prey_rate = float(input("- The rate of destruction of prey by predators: "))
predator_mortality_rate = float(input("- The rate of predator mortality: "))
increase_predator_rate = float(input("- The rate of predator increase through prey consumption: "))
prey_init = int(input("- The initial prey popolation: ")) # y_0
predators_init = int(input("- The initial predators popolation: ")) # x_0
period = int(input("- A period of time between the init and the end, in years: "))

def nature_revamp (a=0.1, b=0.01, c=0.01, d=0.00002, x_0=1000, y_0=20, t_max=2):
  t = 0 # Init of the period
  dt = 0.12 # Variation rate of period
  x = x_0
  y = y_0

  results = [(x, y)]
  while t < t_max:
    dx = x * (a - b * y) * dt
    dy = y * (-c + d * x) * dt
    print(dy)
    x += dx
    y += dy
    t += dt
    results.append((round(x, 2), round(y, 2)))

  print("Here you can see a detailed timeline of variations:\n")
  print(results)

nature_revamp(
  growth_prey_rate,
  destruction_prey_rate,
  predator_mortality_rate,
  increase_predator_rate,
  prey_init,
  predators_init,
  period)

print("\n")
