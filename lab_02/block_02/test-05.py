## ENROLMENT ##

print("\n")
print("## ENROLMENT ##")

print("Now we can try to order to students id")
print("At PoliTO all students id are like this `s123456`\n")
code_1_input = input("Provide a valid student id: ")
code_2_input = input("Provide a second student id: ")

code_1 = int(code_1_input[1:])
code_2 = int(code_2_input[1:])
min_value = min(code_1, code_2)
max_value = max(code_1, code_2)

print(f"The ids ordered would be: [{min_value}, {max_value}]\n")

print("Alter method for more than two would be: ")
student_ids = [code_1_input[1:], code_2_input[1:], 's439012'[1:]]
sortedValue = sorted(student_ids)
print(f"The ids sorted with more than 2: {sortedValue}")


print("\n")
