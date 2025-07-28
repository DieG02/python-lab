## TWO NUMBERS, ALL OPERATIONS ##

print("\n")
print("## TWO NUMBERS, ALL OPERATIONS ##")

print("In this test, we will to eval all the Python basic operations, so...\n")
a_input = input("Please enter a real number A: ")
a = int(a_input)
b_input = input("Please enter a real number B: ")
b = int(b_input)

print("So here you have all the python operations between:", a, "&", b, "\n")
print(f"{'Addition:':<16}", a + b)
print(f"{'Subtraction:':<16}", a - b)
print(f"{'Product:':<16}", a * b)
print(f"{'Average value:':<16}", (a + b) / 2)
print(f"{'Absolute value:':<16}", abs(a + b))
print(f"{'Module value:':<16}", a % b)
print(f"{'Max:':<16}", max(a, b))
print(f"{'Min:':<16}",min(a, b))

print("\n")