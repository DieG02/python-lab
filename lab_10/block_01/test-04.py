## HOTEL MANAGER ##
import os

print("\n")
print("## HOTEL MANAGER ##")
print("")

def is_float(value):
  try:
    float(value)  # Attempt to convert the string to a float
    return True   # If successful, it's a float
  except ValueError:
    return False  # If an error occurs, it's not a float
      
def main():
  filename = input("Enter file to analyse: ")
  validate_file(filename)

def validate_file(filename: str) -> None:
  # File structure: length = 4
  #) the name of the customer; the service sold; the amount paid [float]; the date of the event;
  basename = os.path.basename(__file__).split(".")[0]
  base = os.path.join("lab_10", "block_01", "utils", basename)
  
  print("")
  summary = dict()
  with open(f"{base}/{filename}", "r") as file:
    for i, raw in enumerate(file, start=1):
      fields = raw.strip().split(";")
      fields.remove("")
      if len(fields) != 4:
        print(f"Missing field in line {i}, please verify {filename} and try again")
        return
      elif not is_float(fields[2]):
        print(f"Detect a non `float` value in line {i}, please verify {filename} and try again")
        return
        
      [name, service, amount, date] = fields
      service = service.strip()
      amount = amount.strip()
      if service in summary:
        summary[service] += float(amount)
      else:
        summary[service] = float(amount)
        
  for key in summary:
    print(f"Service: {key:<10} | Subtotal: €{round(summary[key], 2)}")

main()
print("\n")
