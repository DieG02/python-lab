## ERATOSTHENES' SIEVE ##
import math
# NOTE: You can also use `int(n**0.5)`, it's valid if libraries are not allowed

print("\n")
print("## ERATOSTHENES' SIEVE ##")
print("")

def main():
  number = input("Enter a numbers, we'll calculate all the primes: ")
  result =  get_prime_numbers(int(number))
  print("")
  print(f"The final result is:\n{result}")


def get_prime_numbers(n: int) -> list[int]:
  # NOTE: You can use `set` & `range` without `for in`
  all = set([i for i in range(2, n + 1)])
  count = 2
  
  print("These are the removed multipliers:\n")
  while count <= int(math.sqrt(n)):
    # We use count * 2 to avoid deleting the first prime, if it's prime
    current = set(range(count * 2, n + 1, count))
    print(current)
    all = all.difference(current)
    count += 1
  return sorted(all)

main()
print("\n")
