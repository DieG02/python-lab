## NOMS DES PAYS ##

print("\n")
print("## NOMS DES PAYS ##")

exceptions = ['belize', 'cambodge', 'mexique','mozambique', 'zaïre', 'zimbabwe']
vowels = ['a', 'e', 'i', 'o', 'u']
# Rules
# -s
# vocals
# -e exception
# femi
# masc

fr_country = input("Provide to our program a nome of a country in french: ").lower()
# print(fr_country[:1], fr_country[-1:], fr_country, fr_country in exceptions)

phrase = ""

if fr_country[-1:] == 's':
  phrase = "les " + fr_country
elif fr_country[0] in vowels:
  phrase = "l'" + fr_country
elif (fr_country[-1] != 'e') | (fr_country in exceptions):
  phrase = "le " + fr_country
else:
  phrase = "la " + fr_country
  
print(f"In french we'd say: {phrase}")
print("\n")
