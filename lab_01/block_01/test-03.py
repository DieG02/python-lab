## OVER THE STREET ##

print("\n")
print("## OVER THE STREET ##")

distance = 12 # distance house-work [km]
period = 3 # weeks [7]
counter_input = input(f"How many km did you do in the last {period * 7} days: ") # kilometre counter [km]
counter = int(counter_input)
work = 3 # days of work [3/7]

working_days = period * work # 9 days in 3 weeks
work_use = distance * 2 * working_days
personal_use = counter - work_use

if work_use < counter:
  print(f"In {counter} km, you use your car:")
  print(f"{round((work_use / counter) * 100, 2)}% for work")
  print(f"{round((personal_use / counter) * 100, 2)}% for personal use")
else:
  print("Something is missing...")
