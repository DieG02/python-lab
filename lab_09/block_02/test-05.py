## DISCOUNT TO CUSTOMERS ##

print("\n")
print("## DISCOUNT TO CUSTOMERS ##")
print("")

# Input prices
# Input is_pet -> Y / N
# El cajero introduce todos los precios de la compra
# Requisitos para el descuento:
# - Al menos un True en is_pet (hay un animal como mínimo)
# - Al menos 5 productos (5 False como mínimo)

def main():
  prices = list()
  is_pet = list()
  stop = False
  
  while not stop:
    price = input("\nAdd a new product price: €")
    if price != "-1":
      prices.append(float(price))
      type = input("Is an animal? Enter Y(Yes) \ N(No): ").upper()
      is_pet.append(True if type == "Y" else False)
    else:
      stop = True
      
  amount = discount(prices, is_pet)
  print(f"\nThe discount in your case is €{round(amount, 2)}")

def discount(prices: list, is_pet: list) -> float:
  if is_pet.count(False) < 5:
    print("\nThere are not enough items for a discount, we sorry :(")
    return 0
  elif True not in is_pet:
    print("\nYou must to pick at least one pet :(")
    return 0
  else:
    subtotal = 0
    for i, price in enumerate(prices):
      if not is_pet[i]:
        subtotal += price
    return subtotal * 0.2 # 20% discount if everithing is okay

main()
print("\n")