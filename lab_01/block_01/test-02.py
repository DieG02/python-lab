## SEASONS ##

print("\n")
print("## SEASONS ##")

month = int(input("Enter a month number: "))
day = int(input("Enter a day number: "))

# Seasons list
seasons = ["Winter", "Spring", "Summer", "Fall"]
current = 0

if (month >= 1) & (month <= 3):
  current = 0
elif (month >= 4) & (month <= 6):
  current = 1
elif (month >= 7) & (month <= 9):
  current = 2
elif (month >= 10) & (month <= 12):
  current = 3

if (month%3 == 0) & (day >= 21):
  current = (current + 1)%4
print(current)
print("The current season is ", seasons[current])


