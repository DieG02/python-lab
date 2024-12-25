## BAR CHART ##

print("\n")
print("## BAR CHART ##")
print("")

def main():
  values = input("Enter values to print a bar chart, use `SPACE` as separator: ")
  arr = values.split(' ')
  for _, el in enumerate(arr):
    print("*" * int(el))

main()
print("\n")
