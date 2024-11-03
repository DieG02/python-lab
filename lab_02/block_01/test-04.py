## HYBRID THEORY ##

print("\n")
print("## HYBRID THEORY ##")

print("We'll evaluate buying a new car, in this case we'll pay attention to the following items: \n")
print("  1) Price difference between Hybrid Car and Combustion Car")
print("  2) Use rate, the media will be 30.000km by year for all of them")
print("  3) Fuel cost")
print("  4) What is the litre km ratio of each one")
print("  5) How much will cost them to resell in 5 years")
print("\nSo, first of all...")

print("Do you have any models in mind or preffer a quick comparation between combustion, hybrid & electric car?")
custom_choose = input("Press Y if you wanna input data handly or F for a quick comparation: ")


def calculate_resale_value(initial_cost, depreciation_rate=0.18, years=5):
  return initial_cost * (1 - depreciation_rate) ** years

def calculate_fuel_cost(annual_distance, fuel_efficiency, fuel_price, years=5):
  return (annual_distance / fuel_efficiency) * fuel_price * years

def calculate_total_cost(
  initial_cost = None, 
  annual_distance = 30000,
  fuel_price = None,
  fuel_efficiency = None,
  depreciation_rate = 0.18,
  years = 5,
  **kwargs):
  
  if kwargs:
    initial_cost = kwargs.get('price', initial_cost)
    fuel_price = kwargs.get('fuel_cost', fuel_price)
    fuel_efficiency = kwargs.get('efficiency', fuel_efficiency)
    
  # print(initial_cost, annual_distance, fuel_price, fuel_efficiency, depreciation_rate, years)
  resale_value = calculate_resale_value(initial_cost, depreciation_rate, years)
  fuel_cost = calculate_fuel_cost(annual_distance, fuel_efficiency, fuel_price, years)
  total_cost = (initial_cost - resale_value) + fuel_cost
  return round(total_cost, 2)


if((custom_choose == "Y") | (custom_choose == "y") | (custom_choose == "yes") | (custom_choose == "YES")):
  car_a_input = input("Please provide the price of an Hybrid Car Model 2024: €")
  car_b_input = input("Please provide the price of an Combustion Car Model 2024: €")
  car_a = int(car_a_input)
  car_b = int(car_b_input)
  
  # Calculate for hybrid
  hybrid_total_cost = calculate_total_cost(car_a, 30000, 1.6, 20)
  # Calculate for gas
  gas_total_cost = calculate_total_cost(car_b, 30000, 1.6, 15)
  print("So the cost in 5 years of ownership are the following: ")
  
  print("")
  print(f"{'Hybrid Car':^20}|{'Combustion Car':^20}")
  print(f"{'€' + str(hybrid_total_cost):^20}|{('€' + str(gas_total_cost)):^20}")
  
  
else:
  research = {
    "car_a": {
      "model": "Nissan Ariya",
      "type": "Electric",
      "year": 2024,
      "price": 52555,
      "fuel_cost": 0.25, # Price per kWh in €
      "efficiency": 6.67, # km per kWh for electric vehicle
      "brand": "Nissan"
    },
    "car_b": {
      "model": "Toyota Grand Highlander Hybrid Max",
      "type": "Hybrid",
      "year": 2024,
      "price": 52000,
      "fuel_cost": 1.6,
      "efficiency": 20,
      "brand": "Toyota"
    },
    "car_c": {
      "model": "Hyundai Santa Fe",
      "type": "Combustion",
      "year": 2024,
      "price": 43000,
      "fuel_cost": 1.6,
      "efficiency": 15,
      "brand": "Hyundai"
    }
}
  
  print("So we did a quick research about prices/models, and we find out: ")
  # Calculate for electric
  electric_total_cost = calculate_total_cost(**research["car_a"])
  # Calculate for hybrid
  hybrid_total_cost = calculate_total_cost(**research["car_b"])
  # Calculate for gas
  gas_total_cost = calculate_total_cost(**research["car_c"])
  print("So the cost in 5 years of ownership are the following: ")
  
  print("")
  print(f"{'Electric Car':^20}|{'Hybrid Car':^20}|{'Benzine Car':^20}")
  print(f"{'€' + str(electric_total_cost):^20}|{'€' + str(hybrid_total_cost):^20}|{('€' + str(gas_total_cost)):^20}")
 

print("")