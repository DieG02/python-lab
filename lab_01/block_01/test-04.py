## ADDONS ##

print("\n")
print("## ADDONS ##")

length_input = input("Please enter the length of the floor [m]:  ")
width_input = input("Please enter the width of the floow [m]: ")
length = int(length_input) * 10 # 100cm / 10cm
width = int(width_input) * 10 # 100cm / 10cm
area = length * width
amount = int(area/2)

print("")
print("To cover", area ,"m^2 you need", amount, "white pieces &", amount, "black pieces")
print("Here you have a map of how to install them: ")
print("\n")

for i in range(length):
  row = ""
  for j in range(width):
    if (i + j) % 2 == 0:
      row += "[B]"
    else:
      row += "[W]"
    row += " "
  print(row)