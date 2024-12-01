## OUT OF RANGE HANDLING ERROR ##
# NOTE: There are types based on error:
# - IndexError: Access an index that is out of range in a sequence (list, tuple, string)
# - KeyError: Access a dictionary key that doesn’t exist
# - TypeError: Operation or function is applied to an object of inappropriate type
# - ValueError: Function receives an argument of the right type but an inappropriate value
# - NameError: Use a variable or function that hasn’t been defined
# - AttributeError: Access an attribute or method that doesn’t exist for an object
# - ImportError: Module or name within a module can’t be imported
# - RuntimeError: Something goes wrong that doesn’t fall into any other category of exceptions

print("\n")
print("## OUT OF RANGE HANDLING ERROR ##")

def main():
  out_of_range()

def out_of_range():
  list_a = [1, 2, 3, 4, 5]
  # print(list_a[6]) # Throws `out of range` error
  try:
    element = list_a[6]
    print(element)
  except IndexError as type:
    print(f"The index of the list is out of range, try some value between [{0},{len(list_a) - 1}]")
    print(f"Type: `{type}` error")

main()
print("\n")
