## ATM: Automatic Teller Machine ##

print("\n")
print("## ATM: Automatic Teller Machine ##")

print("For this test we'll simulate an ATM")
times = 0
while(times < 3):
  pin = input("\nWelocome to Unicredit, please enter your PIN: ")
  real_pin = '1234'
  times += 1
  
  if(pin == real_pin): 
    print("Well done!")
    break
  elif (3-times) > 0:
    print(f"Wrong PIN, you have {3 - times} tries more")
  else:  
    print(f"Your bank account is blocked!")
    break
    
print("\n")
