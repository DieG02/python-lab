## WAVELENGTH ##

print("\n")
print("## WAVELENGTH ##")

def wavelength():
  print("Wavelength to Electromagnetic Spectrum Converter")
  print("Converts a given wavelength to its corresponding electromagnetic wave type")
  entry = input("Enter a wavelength, you can also use `1.23e-7` notation: ")
  wave_type = ""

  # key: (min, max)
  waves = {
    "radio_waves":    (10**-1,  float('inf')),
    "microwaves":     (10**-3,  10**-1),
    "infrared":       (7*10**-7,  10**-3),
    "visible_light":  (4*10**-7,  7*10**-7),
    "ultraviolet":    (10**-8,  4*10**-7),
    "x-rays":         (10**-11,  10**-8),
    "gamma_rays":     (-float('inf'),  10**-11),
  }
  
  # We set a default value in case entry doesn't contain `e`
  base, power = "0", "0"
  if "e" in entry:
    base = float(entry.split("e")[0])
    power = int(entry.split("e")[1])
  else:
    base = float(entry)
  
  for w_type in waves:
    min, max =  waves[w_type]
    value = base*10**power
    
    if min <= value and value < max:
      wave_type = " ".join(w_type.split("_"))
      break
  
  print(f"\nThe wavelength {entry} belongs to {wave_type.upper()}")
  
wavelength()
print("\n")
