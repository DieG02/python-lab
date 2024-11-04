## PRIME NUMBERS 1 ##

print("\n")
print("## PRIME NUMBERS 1 ##")

def is_prime_number():
  print("For this test we will tell you if a number it's prime or not")
  num = int(input("Enter a number: "))
  index = 1
  arr = []
  
  while index <= num:
    if num % index == 0:
      arr.append(index)
    index += 1
    
  print(f"The number {num} {'is not prime' if len(arr) > 2 else 'is prime'}")
  
is_prime_number()
print("\n")
