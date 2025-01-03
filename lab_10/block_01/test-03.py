## FILE BROWSER ##
import os

print("\n")
print("## FILE BROWSER ##")
print("")

def main():
  basename = os.path.basename(__file__).split(".")[0]
  base = os.path.join("lab_10", "block_01", "utils", basename)
  print(f"We are reading files from the path {base}")
  entry = input("Wich files do you want to analyse? Use `,` as separator: ")
  word = input("Enter a word to browser: ")
  files = entry.split(",")
  
  template = list()
  # Read each file and add to a template if found the word
  for i in range(len(files)):
    filename = files[i].strip()
    with open(f"{base}/{filename}", "r") as file:
      for index, line in enumerate(file, start=1):
        if word in line:
          template.append({
            "filename": filename,
            "line_number": index,
            "line": line.strip()
          })
  
  if not len(template):
    print(f"\nNo results found for `{word}`")
    return None
  
  aux = ""
  for _, match in enumerate(template):
    # Only for add a line-break between different files
    if aux != match['filename']:
      print("")
      aux = match['filename']
    print(f"{match['filename']}: {match['line']}")

main()
print("\n")
