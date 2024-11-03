## DIGITS ##

print("\n")
print("## DIGITS ##")

print("In this test, we will try to decompose a 5 digits number\n")
number_input = input("Provide a 5 digis number (be aware of the length): ")

try:
  number = int(number_input)
  if isinstance(number, int) & (len(number_input) == 5): 
    for i in range(5):
      print(number_input[i])
except ValueError:
  print("Do u enjoy trolling?")
  print("Or don't you know what is a number?")
  print("Anyways, here is the splitted text: ")
  for i in range(len(number_input)):
    print(number_input[i])
    
print("")