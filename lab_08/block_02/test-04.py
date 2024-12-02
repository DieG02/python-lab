## SPRING ##

print("\n")
print("## SPRING ##")

def main():
  # Parameters
  k = 10  # Spring constant (N/m)
  m = 1   # Mass (kg)
  x = 0.5 # Initial displacement from equilibrium (m)
  v = 0   # Initial velocity (m/s)
  delta_t = 0.01 # Time step (s)
  time = 5 # Total simulation time (s)
  
  # Simulation
  t = 0
  positions = []  # To store positions for plotting
  velocities = [] # To store velocities for plotting
  times = []      # To store time steps for plotting
  
  parameters = {
    "k": k,
    "m": m,
    "x": x,
    "v": v,
    "delta_t": delta_t,
    "time": time
  }
  simulations = {
    "t": t,
    "positions": positions,
    "velocities": velocities,
    "times": times
  }
  calculate(parameters, simulations)
  
def calculate(parameters, simulations):
  k, m, x, v, delta_t, time = parameters.values()
  t, positions, velocities, times = simulations.values()
  
  while t <= time:
    # Calculate the restoring force and acceleration
    F = -k * x
    a = F / m
    
    # Update velocity and position
    v = v + a * delta_t
    x = x + v * delta_t
    
    # Store the results for analysis
    positions.append(x)
    velocities.append(v)
    times.append(t)
    
    # Increment time
    t += delta_t
    
  # Output the results (you can also plot them)
  for i in range(len(times)):
    print(f"Time:{str(round(times[i], 2)) + 's':>10}  |  Position: {str(round(positions[i], 2)) + 's':>10}  |  Velocity: {str(round(velocities[i], 2)) + 's':>10}m/s")

main()
print("\n")
