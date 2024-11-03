## CHARACTERS ##

print("\n")
print("## CHARACTERS ##")

print("This is a string problem and how manage spaces... easy!")
word = input("Enter a loooong word: ")

print(f"{word[:3]}{'...' if word[3:6] else '' }{word[6:]}")

print("\n")
