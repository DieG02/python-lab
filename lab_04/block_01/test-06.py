## PRIME NUMBERS 2 ##
from module_05 import is_prime_number

print("\n")
print("## PRIME NUMBERS 2 ##")

def get_all_prime_numbers():
  print("For this test you can enter a number and we show you all prime numbers\n")
  num = int(input("Enter a number: "))
  all_primes = []
  
  for value in range(2, num):
    if is_prime_number(value):
      all_primes.append(value)
      # print(value)
      
  print(all_primes)
  
get_all_prime_numbers()
print("\n")
