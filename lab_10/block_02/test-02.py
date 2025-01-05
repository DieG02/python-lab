## UNIVERSITARY NOTEBOOK ##
import os

print("\n")
print("## UNIVERSITARY NOTEBOOK ##")
print("")

def main():
  # IDs valid: 16753, 21886, 23478, 35987, 45786, 46892, 47896
  id = input("Enter your student ID: ")
  classes = get_all_classes()
  marks = get_my_classes(id, classes)
  print(f"\nStudent ID: {id}\n")
  for _, el in enumerate(marks):
    print(f"{el['code']} {el['mark']}")
  

def get_all_classes() -> list[str]:
  path = os.path.join("lab_10/block_02/utils", "test-02", "classes.txt")
  with open(path, "r") as all_classes:
    classes = list()
    for _, subject in enumerate(all_classes):
      classes.append(subject)
    return classes

def get_my_classes(id: str, classes: list[str]) -> list[dict]:
  base = os.path.join("lab_10/block_02/utils", "test-02", "exams")
  marks = list()
  for _, code in enumerate(classes):
    code = code.strip() # Just in case, to ensure a clean subject code from `classes.txt`
    if not os.path.exists(f"{base}/{code}.txt"):
      continue # Maybe some teachers don't submit their results yet
    
    with open(f"{base}/{code}.txt", "r") as subject:
      for _, result in enumerate(subject):
        result = result.strip()
        if id in result:
          marks.append({
            "code": code,
            "mark": result.split(" ")[1]
          })
          break # Because you will have only one mark in each file
  return marks
          

main()
print("\n")
