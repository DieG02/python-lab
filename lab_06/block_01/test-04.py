## BANK ACCOUNT CREDIT ##

print("\n")
print("## BANK ACCOUNT CREDIT ##")

def get_my_balance(period, initial, annual_rate):
  rate = round(annual_rate / 100, 2)
  return initial + (period * rate * initial)

period = 10; initial_amount = 25000; increase_rate = 12
balance = get_my_balance(period, initial_amount, increase_rate)
print(f"My balance from €{initial_amount} for {period} years with increase rate of {increase_rate}% by year is: {balance}")
print("\n")
