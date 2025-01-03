## THE BEST CUSTOMER ##

print("\n")
print("## THE BEST CUSTOMER ##")
print("")

def is_decimal(string):
  try:
    round(float(string), 2)
    return True
  except ValueError:
    return False

def main():
  customers = list()
  sales = list()
  
  while True:
    amount = input("Enter the amount spent by the client (0 to end): ")
    if amount == "0" or not is_decimal(amount):
      break
    name = input("Enter the client's name: ")
    sales.append(float(amount))
    customers.append(name)
  name_of_best_customer(sales, customers)
    
def name_of_best_customer(sales: list[float], customers: list[str]) -> str:
  """
  Identify the name of the best customer
  :param `sales`: the list of sale amounts
  :param `customers`: the names of the customers
  :return: the name of the customer with the highest sale amount
  """
  largest = max(sales)
  for i, el in enumerate(sales):
    if el == largest:
      print(f"\nThe best customer of today is {customers[i]} with an amount of €{largest}")
      return customers[i]

main()
print("\n")
