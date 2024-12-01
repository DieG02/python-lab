## LIST MERGE ##

print("\n")
print("## LIST MERGE ##")

def main():
  a = [1, 9, 4, 7, 9, 4, 16, 9, 11]
  b = [3, 19, 11, 6, 1]
  merge(a, b)

def merge(a, b):
  length = len(a) if len(a) < len(b) else len(b)
  c = []
  for i in range(length):
    c.extend([a[i], b[i]])
  c.extend(a[length:])
  c.extend(b[length:])
  print(c)

main()
print("\n")
