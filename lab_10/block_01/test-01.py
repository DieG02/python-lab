## READ & WRITE FILES ##
import os
# NOTE: This is the first lab with `file` managing
# In this case we only `read` and `write` line by line with minnor changes

print("\n")
print("## READ & WRITE FILES ##")
print("")

def main():
  # root = os.getcwd() # it's not necessary if we use relative path (from this working directory)
  filename = os.path.basename(__file__).split(".")[0]
  base = os.path.join("lab_10", "block_01", "utils")

  # Read the input.txt line by line
  with open(f"{base}/{filename}/input.txt", 'r') as file:
    # template = file.read()
    template = ""
    for index, line in enumerate(file, start=1):
      template += f"/*{index}*/ {line.strip()}\n"
      print(f"/*{index}*/", line.strip())
      
  # Write the formatted prompt at output.txt
  with open(f"{base}/{filename}/output.txt", 'w') as file:
    file.write(template)
          
main()
print("\n")
