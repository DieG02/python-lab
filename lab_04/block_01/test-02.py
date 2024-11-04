## STRING ANALISIS ##

print("\n")
print("## STRING ANALISIS ##")

def string_analisis():
  string = input("Provide a string: ")
  upper_case = string.upper()
  even_case = ""
  vowel_case = ""
  number_case = 0
  array_case = []
  
  vowels = set(['a', 'e', 'i', 'o', 'u'])

  for index, ch in enumerate(string):
    flag = ch.lower() in vowels
    even_case += ch if index%2 == 0 else ""
    vowel_case += ch if flag else "_"
    number_case += 1 if ch.isnumeric() else 0
    if flag: array_case.append(index)
  
  print(f"""
    {'Uppdercase:':<16} {upper_case}
    {'Even:':<16} {even_case}
    {'Vowels:':<16} {vowel_case}
    {'Numbers:':<16} {number_case}
    {'Array:':<16} {array_case}
  """)

string_analisis()
print("\n")
