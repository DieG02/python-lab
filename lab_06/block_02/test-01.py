## ONG BOT ##

print("\n")
print("## ONG BOT ##")


def calculate_assignment(balance, sons):
  benefits = [1000, 1500, 2000]
  if balance > 40000:
    return 0
  elif balance >= 30000:
    return benefits[0] * sons if sons >= 3 else 0
  elif balance >= 20000:
    return benefits[1] * sons if sons >= 2 else 0
  else: 
    return benefits[2] * sons


def get_social_assignments():
  print('With this program you will have all the assignments in a few\n')
  print('How to use it:\nFirst you add the family `balance` (ex. 30000)\nThen with an empty space add amount of sons')
  print('At the end you will have something like: 3000 2\n')
  
  values = ['']
  while values:
    values_input = input("Get social assignment of: ")
    if values_input == -1:
      break
    
    values = values_input.split(' ')
    assignment = calculate_assignment(float(values[0]), int(values[1]))
    print(f"The assignment for this family is: {assignment:<10}\n")
    
get_social_assignments()
    
print("\n")
