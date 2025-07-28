## APPOINMENTS ##

print("\n")
print("## APPOINMENTS ##")

start_1 = int(input("First event inits at: "))
end_1 = int(input("First event ends at: "))
start_2 = int(input("Second event inits at: "))
end_2 = int(input("Second event ends at: "))

# We need to confirm that they are numbers and they are [0, 24)
first_event = 0 <= start_1 < 24 and 0 <= end_1 < 24
second_event = 0 <= start_2 < 24 and 0 <= end_2 < 24

if first_event and second_event:
  if start_1 > start_2:
    s = start_1
  else:
    s = start_2
    
  if end_1 < end_2:
    e = end_1
  else:
    e = end_2

  if s < e:
    print("The events overlap")
  else:
    print("The events don't overlap")
else:
  print("Invalid inputs, try again!")



