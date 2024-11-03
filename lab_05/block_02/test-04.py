## ELECTRONIC EXERCISE ##

print("\n")
print("## ELECTRONIC EXERCISE ##")

print(
"""
Let's vary the number of turns with an interval of 0.1 to find
the best configuration for a circuit consisting of:
- An amplifier
- A transformer
- A speaker
""")

details = input("This is a loong process, do you want to see it in detail? Y / N: ")

v_s = 40 # volts [v]
r_0 = 20 # omhs [Ω]
r_s = 8 # omhs [Ω]
n_min = 0.01 # integer
n_max = 2 # integer
delta_n = 0.01 # Δn

max_values = {
  "coil_ratio": 0,
  "speaker_power": 0
}

n = n_min
if (details == 'Y') | (details == 'y'):
  print(f"{'S_Power':^12}|{'Nº Coils':^10}")
  print(f"{'-'*12:^12}+{'-'*10:^10}")
  
while n <= n_max:
  num = n * v_s # Numerator
  denum = (n**2) * r_0 + r_s # Denumerator
  p_s = r_s * ((num / denum)**2) # Speaker Power
  
  if p_s > max_values["speaker_power"]:
    max_values["coil_ratio"] = round(n, 4)
    max_values["speaker_power"] = round(p_s, 4)
  if (details == 'Y') | (details == 'y'):
    print(f"{round(p_s, 4):^12}|{round(n, 2):^10}")
  n += delta_n

print("The best performance can be found at:")
print(f"Coil Ratio = {max_values['coil_ratio']}")
print(f"Speaker Power = {max_values['speaker_power']}")

print("\n")
