## SCHOOL MARKS ##

print("\n")
print("## SCHOOL MARKS ##")

def marks():
  note = input("Enter a note in letter [A, B, C, D, F]: ")
  note = note.upper()
  result = float()
  diff = { "-": -0.3, "+": 0.3 }
  notes = dict({ "A": 4.0, "B": 3.0, "C": 2.0, "D": 1.0, "F": 0.0 })
  
  key = note[0]
  sign = ""
  if len(note) == 2:
    sign = note[1]
    
  if note == "F-" or note == "F+":
    print("Invalid input")
    return
  elif sign:
    result = notes[key] + diff[sign]
    result = min(result, 4.0)
  else:
    result = notes[key]
    
  print(f"Numerial mark is: {result}")
  return

marks()
print("\n")
