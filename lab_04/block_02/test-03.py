## VERTICAL SHOT ##

print("\n")
print("## VERTICAL SHOT ##")

print("")

def vertical_shot():
  DELTA_T = 0.01
  G = 9.81
  v_0 = int(input("v_0: ")) # 100
  s_0 = 0
  v = v_0
  s = 0
  
  print(f"{round(s, 2):^10} | {round(v, 2):^10} | {round(DELTA_T, 2):^10}")
  while v >= -v_0:
    v = v_0 - G * DELTA_T
    s = s_0 + v_0 * DELTA_T
    DELTA_T += 0.01
    print(f"{round(s, 2):^10} | {round(v, 2):^10} | {round(DELTA_T, 2):^10}")

vertical_shot()

print("\n")
