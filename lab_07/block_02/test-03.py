## BULGARIAN SOLITARIE ##
# RULES: 45 cards, in random queues. Each move, remove one card of all queues

print("\n")
print("## BULGARIAN SOLITARIE ##")

def main():
  sort_card()
  
def sort_card():
  initial_state = [20, 5, 1, 9, 10]
  end_state = [1, 2, 3, 4, 5, 6, 7, 8, 9]
  flag = set(initial_state) == set(end_state)
  print(initial_state)
  
  while not flag:
    current = initial_state
    initial_state = []
    for i in range(len(current)):
      value = current[i] - 1
      initial_state.append(value) if value > 0 else None
    initial_state.append(len(current))

    flag = set(initial_state) == set(end_state)
    print(initial_state)

main()
print("\n")
