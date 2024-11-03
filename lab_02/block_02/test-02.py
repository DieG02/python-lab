## PHONE NUMBER ##

print("\n")
print("## PHONE NUMBER ##")

print("In this test, we will format a 10 digits number into a phone number")
print("We'll use this format `(415) 222-5555`, so...")
number = input("Provide a 10 digits phone number, like this `4152225555`: ")

print("This number is formated like:", f"({number[:3]}) {number[3:6]}-{number[6:]}")

print("\n")
