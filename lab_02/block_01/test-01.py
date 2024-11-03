## TWO NUMBERS, ALL OPERATIONS ##

print("\n")
print("## TWO NUMBERS, ALL OPERATIONS ##")

print("In this test, we will to eval all the Python basic operations, so...\n")
a_input = input("Please enter a [R] real number A: ")
a = int(a_input)
b_input = input("Please enter a [R] real number B: ")
b = int(b_input)

print("So here you have all the python operations between:", a, "&", b, "\n")
print(f"{'Sum:':15}", a + b)
print(f"{'Difference:':15}", a - b)
print(f"{'Product:':15}", a * b)
print(f"{'Division:':15}", round(a / b, 4))
print(f"{'Mean Value:':15}", (a + b)/2)
print(f"{'Residual:':15}", a % b)
print(f"{'Module:':15}", abs(a - b))
print(f"{'Max:':15}", max(a, b))
print(f"{'Min:':15}", min(a, b))

print("\n")