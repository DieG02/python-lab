## SORT & MERGE LIST ##

print("\n")
print("## SORT & MERGE LIST ##")

def main():
  a = [1, 9, 4, 7, 9, 4, 16, 9, 11]
  b = [3, 19, 11, 6, 1]
  sorted_merge(a, b)

def sorted_merge(a, b):
  c = a
  c.extend(b)

  for _ in range(len(c)):
    for j in range(len(c) - 1):
      current = c[j]
      next = c[j+1]
      if current >= next:
        flag = current
        c[j] = next
        c[j+1] = flag
        
  print(c)

main()
print("\n")
