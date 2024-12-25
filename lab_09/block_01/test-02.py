## HIDDEN RULES ##

print("\n")
print("## HIDDEN RULES ##")
print("")

def main():
  data = list()
  rule_1(data)
  rule_2(data)
  rule_3(data)
  rule_4(data)
  rule_5(data)
  rule_6(data)
  rule_7 (data)

def rule_1(arr: list) -> list:
  data = arr.copy()
  for i in range(1, 10 + 1):
    data.append(i)
  print("rule_1", data, "\n")

def rule_2(arr: list) -> list:
  data = arr.copy()
  for i in range(0, 10):
    data.append(i * 2)
  print("rule_2", data, "\n")

def rule_3(arr: list) -> list:
  data = arr.copy()
  for i in range(1, 10 + 1):
    data.append(i ** 2)
  print("rule_3", data, "\n")

def rule_4(arr: list) -> list:
  data = arr.copy()
  for i in range(1, 10 + 1):
    data.append(0)
  print("rule_4", data, "\n")

def rule_5(arr: list) -> list:
  # Doesn't have a rule to follow
  data = [1, 4, 9, 16, 9, 7, 4, 9, 11]
  print("rule_5", data, "\n")

def rule_6(arr: list) -> list:
  data = arr.copy()
  for i in range(0, 10):
    data.append(0 if i % 2 == 0 else 1)
  print("rule_6", data, "\n")

def rule_7(arr: list) -> list:
  data = arr.copy()
  for i in range(0, 10):
    data.append(i % 5)
  print("rule_7", data, "\n")

main()
print("\n")
