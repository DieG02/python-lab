# UNIT CONVERTER #

print("\n")
print("## UNIT CONVERTER ##")

sources = [ "ml", "l", "g", "kg", "mm", "cm", "m", "km" ]
targets = [ "fl", "oz", "gal", "lb", "in", "ft", "mi" ]

def unit_converter():
  print("Welcome to the unit converter!")
  print("Choose your starting unit and the unit to convert to")
  source_unit = input(
    f"Enter the source unit ({', '.join(sources)}): "
  ).lower()
  target_unit = input(
    f"Enter the target unit ({', '.join(targets)}): "
  ).lower()
  
  if (source_unit not in sources) or (target_unit not in targets):
    print("Invalid target unit.")
    return
    
  # Check for incompatible conversions
  incompatible_conversions = {
    "ml": ["lb", "in", "ft", "mi"],
    "l": ["lb", "in", "ft", "mi"],
    "g": ["fl", "oz", "gal", "in", "ft", "mi"],
    "kg": ["fl", "oz", "gal", "in", "ft", "mi"],
    "mm": ["fl", "oz", "gal", "lb"],
    "cm": ["fl", "oz", "gal", "lb"],
    "m": ["fl", "oz", "gal", "lb"],
    "km": ["fl", "oz", "gal", "lb"]
  }
  
  if target_unit in incompatible_conversions.get(source_unit, []):
    print(f"Conversion from {source_unit} to {target_unit} is not compatible")
    return
  
  value = float(input("Enter the value to convert: "))
  
  # Conversion factors
  factors = {
    ("ml", "fl"): 0.033814,
    ("l", "gal"): 0.264172,
    ("g", "oz"): 0.035274,
    ("kg", "lb"): 2.20462,
    ("mm", "in"): 0.0393701,
    ("cm", "in"): 0.393701,
    ("m", "ft"): 3.28084,
    ("km", "mi"): 0.621371
  }
  
  # Perform conversion
  key = (source_unit, target_unit)
  if key in factors:
    converted = value * factors[key]
    print(f"\nConverted {value} {source_unit} to {converted:.2f} {target_unit}")
  else:
    print(f"\nNo direct conversion available for {source_unit} to {target_unit}")
    return

unit_converter()
print("\n")
