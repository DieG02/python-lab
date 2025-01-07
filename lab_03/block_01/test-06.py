## DE MORGAN - LOGICAL EXPRESSIONS ##

print("\n")
print("## DE MORGAN - LOGICAL EXPRESSIONS ##")

def de_morgan():
  n = input("Enter an integer, we will evaluate with De Morgan: ")
  x = int(n)
  
  test_1 = not (x > 0 and x < 100)
  test_2 = not (x > 0 or x < 100)
  test_3 = not (x > 0 or 100 < x)
  test_4 = not (x > 0 and x < 100 or x == -1)
  
  print(f"\nNow the results evaluated in n: {n}\n")
  print(f"not (x > 0 and x < 100) is equal to not x > 0 or not x < 100")
  print(f"Test A1 {test_1}, Test B1 {x <= 0 or x >= 100}\n")
  
  print(f"not (x > 0 or x < 100) is equal to not (x > 0 or x < 100)")
  print(f"Test A2 {test_2}, Test B2 {x <= 0 and x >= 100}\n")
  
  print(f"not (x > 0 or 100 < x) is equal to not (x > 0 or 100 < x)")
  print(f"Test A3 {test_3}, Test B3 {x <= 0 and x <= 100}\n")
  
  print(f"not (x > 0 and x < 100 or x == -1) is equal to not (x > 0 and x < 100 or x == -1)")
  print(f"Test A4 {test_4}, Test B4 {x <= 0 or x >= 100 or x == -1}\n")

de_morgan()
print("\n")
