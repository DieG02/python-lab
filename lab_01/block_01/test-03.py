## OVER THE STREET ##

print("\n")
print("## OVER THE STREET ##")

distance = 12 # distance house-work [km]
period = 3 # weeks [7]
counter_input = input(f"How many km did you do in the last {period * 7} days: ") # kilometre counter [km]
counter = int(counter_input)
work = 3 # days of work [3/7]

workingDays = period * work # 9 days in 3 weeks
workUse = distance * 2 * workingDays
personalUse = counter - workUse

if workUse > counter:
  print("Did you sleep at work???")
else:
  print(f"In {counter} km, you use your car:")
  print(f"{round((workUse / counter) * 100, 2)}% for work")
  print(f"{round((personalUse / counter) * 100, 2)}% for personal use")
