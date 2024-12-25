## COMPLEX BAR CHART ##

print("\n")
print("## COMPLEX BAR CHART ##")
print("")

def main():
  values = input("Enter values to print a bar chart, use `SPACE` as separator: ")
  arr = values.split(' ')
  for i, el in enumerate(arr):
    arr[i] = int(el)
    
  ordered = arr.copy()
  ordered.sort()
  min = int(ordered[0])
  print(min)
  
  for _, value in enumerate(arr):
    if value >= 0:
      print(f"{' '*abs(min)}{'*'*abs(value)}")
    else:
      print(f"{' '*abs(min-value)}{'*'*abs(value)}")
      
main()
print("\n")
