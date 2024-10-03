## APPOINMENTS ##

print("\n")
print("## APPOINMENTS ##")

start1 = input("First event inits at: ")
end1 = input("First event ends at: ")
start2 = input("Second event inits at: ")
end2 = input("Second event ends at: ")

if start1 > start2:
  s = start1
else:
  s = start2
  
if end1 < end2:
  e = end1
else:
  e = end2

if s < e:
  print("The events overlap")
else:
  print("The events don't overlap")



