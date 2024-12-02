## AVERAGE LIMIT NUMBERS ##
# NOTE: `inline random matrix`
# [[random.randint(`limit`) for _ in range(`cols`)] for _ in range(`rows`)]
# NOTE: Usage of custom `module` (downscaling, I couldn't upscaling yet)
import random
from utils import printf

print("\n")
print("## AVERAGE LIMIT NUMBERS ##")

def main():
  rows, cols = 4, 5
  matrix = [[random.randint(1, 20) for _ in range(cols)] for _ in range(rows)]
  printf(matrix)
  neighbor_average(matrix, 0, 0)
  neighbor_average(matrix, 0, 4)
  neighbor_average(matrix, 3, 0)
  neighbor_average(matrix, 3, 4)
  neighbor_average(matrix, 1, 2)
  
def neighbor_average(values, row, column):
  total = 0; count = 1; acc = []
  
  print("\n")
  for i in range(-1, 2):
    for j in range(-1, 2):
      if (i != 0 or j != 0) and (row + i >= 0 and column + j >= 0) and (row + i < 4 and column + j < 5):
        current = values[row + i][column + j]
        total += current
        acc.append(current)
        # print(values[row + i][column + j])
        count += 1
  print(f"{'To ignore:':<15}{values[row][column]} | ({column},{row})")
  print(f"{'Neighbors:':<15}{acc}")
  print(f"{'Average:':<15}{round(total/count, 2)}")
main()
print("\n")
