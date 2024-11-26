## THE SAME ELEMENTS ##

print("\n")
print("## THE SAME ELEMENTS ##")

def main():
  a = [1, 4, 9, 16, 9, 7, 4, 9, 11]
  b = [11, 11, 7, 9, 16, 4, 1]
  equals = same_set(a, b)
  if equals:
    print("The list are the same set")
  else:
    print("The list are not equal")

def same_set(a, b):
  set_a = set(a)
  set_b = set(b)
  new_set = set_a.union(set_b)
  return len(new_set) == len(set_a)

main()
print("\n")
