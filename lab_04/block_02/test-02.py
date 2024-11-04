## DIAGNOSTIC IMAGING ##
# NOTE: Fun fact, this was the most mathematical exercise 'till now
import math

print("\n")
print("## DIAGNOSTIC IMAGING ##")

def get_diagnostic():
  # Original Formula: 𝐴 = 𝐴_0 * e^(-𝜆t)  -> 𝜆 = ln (2) / T_(1/2)
  
  # Calculate relative amount of radiation: `A / A_0`
  ln_2 = math.log(2) # If there is only one single parameter is, it uses `ln`
  media_life = 6 # T_(1/2)
  period_of_time = 24 # in hours
  for t in range(period_of_time + 1):
    lambda_val = ln_2 / media_life
    amount = math.e ** (-lambda_val * t)
    print(f"{'Hour ' + str(t) + ':':<12}{round(amount, 2)}")

get_diagnostic()
print("\n")
