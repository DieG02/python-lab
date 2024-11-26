## REMOVE MIN FROM LIST ##
# NOTE: Here we use `None` for an empty var & `float(inf)` for the max value allowed

print("\n")
print("## REMOVE MIN FROM LIST ##")

def main():
  list_example = [3, 4, 10, 3, 1, -4, 8, 9]
  new_list = remove_min(list_example)
  print(f"The new list is: {new_list}")

def remove_min(list):
  if len(list) == 0: return []
  i = None; min = float('inf')
  for index, val in enumerate(list):
    if min > val:
      min = val
      i = index
  return list[: i] + list[i+1 :]

main()
print("\n")
