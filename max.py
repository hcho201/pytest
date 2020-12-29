# Bigger Integer 
def max(a, b):

    if a > b :
        m = a
    else :
        m = b
  
    return m

a = input("Input 1st Integer: ")
b = input("Input 2nd Integer: ")

MAX = max(a, b)
print("Max Integer: " + MAX)

