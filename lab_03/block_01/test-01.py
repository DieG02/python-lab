## TRUE OR FALSE ##
import math

print("\n")
print("## TRUE OR FALSE ##")

def bool_test():
  test_1 = 1 == 1
  test_2 = 1 == 1.0
  test_3 = 2.0 == math.sqrt(4)
  test_4 = '1' == 1
  test_5 = 'ciao' == 'Ciao'
  tests = [test_1, test_2, test_3, test_4, test_5]
  for index, val in enumerate(tests):
    print(f"Test {index + 1}: {val}")
  
bool_test()

print("\n")
