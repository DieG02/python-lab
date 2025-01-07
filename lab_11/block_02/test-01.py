## INCOME PER CAPITA ##
import os
# NOTE: This exercise use `type` in `dict` correctly

print("\n")
print("## INCOME PER CAPITA ##")
print("")

def main():
  print("Welcome to our income per capita manager!\n")
  base = os.path.join("lab_11/block_02", "utils", "test-01")
  
  filename_txt = os.path.join(base, "rawdata_2004.txt")
  filename_csv = os.path.join(base, "rawdata_2021.csv")
  store_old = analyse_txt(filename_txt)
  store_new = analyse_csv(filename_csv)
  stop = False
  
  while not stop:
    country = input("Enter the name of a country or e(exit): ")
    key = country.lower()
    
    # Here we set as first option most recent date
    if key in store_new:
      print("\n> Data from 2021")
      print(f"Country: {country}\nIncomes: ${store_new[key][1:]:>18}\n")
    elif key in store_old:
      print("\n> Data from 2004")
      print(f"Country: {country}\nIncomes: {store_old[key]}\n")
    elif key == "e":
      stop = True
    else:
      print(f"\nWe didn't find any result for {country}, try again\n")
  
  
# NOTE: Keys must be hashable: 
# Immutable types like strings, numbers (int, float), and tuples are valid dictionary keys.
def analyse_txt(filename: str) -> dict[str, int]:
  store = dict()
  file = open(filename, "r")
  
  # This file has a particular separation with "\n"
  for line in file:
    [index, country, value] = line.strip().split("\t")
    store[country.lower()] = value
  return store


def analyse_csv(filename: str) -> dict[str, int]:
  store = dict()
  file = open(filename, "r")
  
  # This file has a particular first line, we must to ignore the header
  for line in file:
    if '","' not in line:
      continue
    [name, _, value, *others] = line.strip()[1:-1].split('","')
    store[name.lower()] = value
  return store


main()
print("\n")
