## EMOJI ##

print("\n")
print("## EMOJI ##")

print("For this test, we'll evaluate your top-3 emoji more used: ")
print("This is only for table creation, not input for user today :c")

ranking = [{
  "name": "Melting Face",
  "code": "U+1FAE0",
  "character": "🫠", 
}, {
  "name": "Freezing Face",
  "code": "U+1F976",
  "character": "🥶", 
}, {
  "name": "Grimacing Face",
  "code": "U+1F62C",
  "character": "😬", 
}]

print("")
print(f"{'Rank':^8}|{'Unicode Nº':^14}|{'Unicode Name':^20}|{'Emoji':^8}")
print(f"{'-'*8}+{'-'*14}+{'-'*20}+{'-'*8}")
for index, emote in enumerate(ranking):
  print(f"{index:^8}|{emote['code']:^14}|{emote['name']:^20}|{emote['character']:^8}")

print("\n")
