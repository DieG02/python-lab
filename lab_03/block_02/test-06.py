## TAX CALCULATOR ##

print("\n")
print("## TAX CALCULATOR ##")

def tax_calculator():
  print("Tax time? Don't panic! Let's crunch some numbers.")
  print("Our friendly tax calculator will help you figure out your taxes.")
  
  response = input("First of all, are you married? Y(yes) / N(not yet): ")
  is_married = response.upper() == "Y"
  incomes_input = input("Now, introduce your incomes: £")
  incomes = int(incomes_input)
  taxes = [0, 16000, 64000] if is_married else [0, 8000, 32000]
  payment = 0
    
  if incomes < taxes[1]:
    payment = incomes * 0.1
  elif incomes < taxes[2]:
    excess = incomes - taxes[1]
    fixed = 1600 if is_married else 800
    payment = excess * 0.15 + fixed
  else:
    excess = incomes - taxes[2]
    fixed = 8800 if is_married else 4400
    payment = excess * 0.25 + fixed
  
  print(f"Your incomes are £{incomes}")
  print(f"For this amount you must to pay £{payment}")

tax_calculator()
print("\n")
