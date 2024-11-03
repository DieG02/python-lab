# rombo = int(input('lato: '))
# for i in range(rombo):
#   val = ''
#   for j in range(i*2 + 1):
#     val += '*'
#   print(' '*(rombo-i) + val, end='')
#   print()
  
# print('*'*(rombo*2 + 1))
# for i in range(rombo):
#   val = ''
#   for j in range((rombo-i)*2 - 1):
#     val += '*'
#   print(' '*(i+1) + val, end='')
#   print()
  
  
rombo = int(input('lato: '))

for i in range(rombo):
  print(' ' * (rombo - i) + '*' * (i * 2 + 1))

print('*' * (rombo * 2 + 1))

for i in range(rombo):
  print(' ' * (i + 1) + '*' * ((rombo - i) * 2 - 1))