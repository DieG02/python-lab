## MATH SHAPES ##
# NOTE: Review all formules
import math

print("\n")
print("## MATH SHAPES ##")

pi = math.pi

def sphere_volume(r):
  vol_sphere = (4/3) * pi * (r ** 3)
  return vol_sphere
  
def sphere_surface(r):
  sup_sphere = 4 * pi * (r ** 2)
  return sup_sphere
  
def cylinder_volume(r, h):
  sup_base = pi * (r ** 2)
  vol_cylinder = sup_base * h
  return vol_cylinder
  
def cylinder_surface(r, h):
  base = 2 * pi * r
  sup_cylinder = base * h
  return sup_cylinder
  
def cone_volume(r, h):
  sup_base = pi * (r ** 2)
  vol_cone = sup_base * (h / r)
  return vol_cone
  
def cone_surface(r, h):
  base = 2 * pi * r
  sup_cone = base * (h / r)
  return sup_cone
  

print("\n")
