## TO THE CINEMA ##

print("\n")
print("## TO THE CINEMA ##")

print("Today, we'll create a system for a litle cinama, allora...")
print("All users can buy at most 4 tickets buy person, 100 in total to sold\n")

tickets = 100
while tickets > 0:
  print(f"Tickets available: {tickets}/100")
  print("Good morning Sr. how many tickets do u want for TASM3?: ")
  ticket = int(input(""))

  if (ticket <= 4):
    print("Here you have gentleman")
    print("Next please")
    print("\n")
    tickets -= ticket
  else:
    print("You can't buy more than 4")
    print("NEEEXT!!!")
    print("\n")

print("\n")
