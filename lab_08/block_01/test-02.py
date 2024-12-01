## LIST BUFFER HANDLER ##

print("\n")
print("## LIST BUFFER HANDLER ##")

def main():
  sort_index()

def sort_index():
  list_example = [4, 0, 1, 9, 7] # [7, 4, 0, 1, 9]
  print(list_example)
  val = list_example.pop()
  list_example.insert(0, val)
  print(list_example)

main()
print("\n")
