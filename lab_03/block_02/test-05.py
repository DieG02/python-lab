## SCHOOL MARKS ##

print("\n")
print("## SCHOOL MARKS ##")

def marks():
  stop = False
  
  while not stop:
    print("Let's turn your numbers into letters!")
    print("Convert your numerical grades to letter grades.")
    note = input("Enter a number between [0.0 - 4.0] or press E(exit): ")
    if note.isalpha():
      stop = True
      break
          
    value = round(float(note) * 100)
    notes = list(["F", "D", "C", "B", "A"])
    index = int(value / 100)
    decimal, sign = value%100, "" 
    
    if decimal >= 15 and decimal < 50:
      sign = "+"
    elif decimal >= 50 and decimal < 85:
      sign = "-"
      index += 1
    elif decimal >= 15:
      index += 1
      
    print(f"{notes[index]}{sign}\n")

marks()
print("\n")
