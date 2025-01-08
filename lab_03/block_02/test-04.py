## LEAP YEAR ##

print("\n")
print("## LEAP YEAR ##")

def calculate():
  print("Let's determine if a year is a leap year!")
  print("Remember that a leap year has 366 days and is used to keep our calendar aligned with the Earth's orbit around the Sun.")
  print("This program allows you to, given a year, determines if it's a leap year!")
  
  year_input = input("Enter a year upper to 1582: ")
  year = int(year_input)
  
  if year >= 1582 and( year % 400 == 0 or (not year % 100 == 0 and year % 4 == 0)):
    print(f"The year {year} is leap")
  else: 
    print(f"The year {year} is not leap")

calculate()
print("\n")
