## DRAWING SHAPES ##

print("\n")
print("## DRAWING SHAPES ##")

def drawing_shapes():
  width = int(input("Provide a number: "))
  sup = ""; inf = ""; square = ""
  
  for i in range(width):
    delta = i * 2 + 1
    shape_sup = "+" * delta + "\n"
    shape_inf = "+" * (width*2 - delta) + "\n"
    
    sup += " " * (width-1 - i) + shape_sup
    inf += " " * i + shape_inf if i != 0 else ""
    
    square += "[]" * width + "\n"
  print(f"{sup}{inf}\n")
  print(square)
  
drawing_shapes()
   

print("\n")
