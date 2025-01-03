## REVERSED FILE ##
import os

print("\n")
print("## REVERSED FILE ##")
print("")

def main():
  filename = os.path.basename(__file__).split(".")[0]
  base = os.path.join("lab_10", "block_01", "utils")
  
  # Read the custom file and add to a template
  with open(f"{base}/{filename}/input.txt", "r") as file:
    print(f"We read the `{base}/{filename}/input.txt` file")
    template = list()
    for line in file:
      template.append(line.strip())
      
  # Create a `copy` and then `reverse` it, then just join with a `line break`
  with open(f"{base}/{filename}/output.txt", "w") as file:
    print(f"We write the `{base}/{filename}/output.txt` file")
    new_template = template.copy()
    new_template.reverse()
    file.write("\n".join(new_template))
      
main()
print("\n")
