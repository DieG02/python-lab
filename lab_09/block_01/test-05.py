## LABELED BAR CHART ##

print("\n")
print("## LABELED BAR CHART ##")
print("")

def main():
  values = input("Build a bar chart, use `leyend-value` to enter values and `SPACE` as separator: ")
  arr = values.split(' ')
  for _, el in enumerate(arr):
    el = el.split('-')
    count = int(el[1])
    spacing = 10
    print(f"{el[0]:>{spacing}}", " "*3,"*"*count)
    
main()
print("\n")
