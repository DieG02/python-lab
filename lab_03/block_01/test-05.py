## LOGICAL EXPRESSIONS ##

print("\n")
print("## LOGICAL EXPRESSIONS ##")

def show_results():
  n = input("Enter an integer, we will evaluate with some expressions: ")
  x = int(n)
  
  test_1 = x > 0 and x < 100
  test_2 = x > 0 or x < 100
  test_3 = x > 0 or 100 < x
  test_4 = x > 0 and x < 100 or x == -1
  
  print(f"\nNow the results evaluated in n: {n}\n")
  print(f"The expression: x > 0 and x < 100 is {test_1}")
  print(f"The expression: x > 0 or x < 100 is {test_2}")
  print(f"The expression: x > 0 or 100 < x is {test_3}")
  print(f"The expression: x > 0 and x < 100 or x == -1 is {test_4}")
  return
  

show_results()
print("\n")
