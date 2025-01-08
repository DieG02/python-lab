# SEASON DETERMINER #

print("\n")
print("## SEASON DETERMINER ##")

def find_season():
  print("Let's determine the season for a given month and day\n")
  month_input = input("Enter the month (1-12): ")
  month = int(month_input)
  day_input = input("Enter the day (1-31): ")
  day = int(day_input)
  
  # Determine the initial season based on the month
  if month in [1, 2, 3]:
    season = "WINTER"
  elif month in [4, 5, 6]:
    season = "SRPING"
  elif month in [7, 8, 9]:
    season = "SUMMER"
  elif month in [10, 11, 12]:
    season = "FALL"
  else:
    print("Invalid month entered.")
    return
  
  # Adjust the season based on additional conditions
  if month % 3 == 0 and day >= 21:  # Check divisibility by 3 and day >= 21
    if season == "WINTER":
      season = "SRPING"
    elif season == "SPRING":
      season = "SUMMER"
    elif season == "SUMMER":
      season = "FALL"
    else:
      season = "WINTER"
  
  # Output the determined season
  print(f"\nThe date {month}/{day} falls in {season}.")

find_season()
print("\n")