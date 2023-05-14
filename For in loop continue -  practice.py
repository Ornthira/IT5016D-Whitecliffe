#practice code for understanding list, for loop and == 
#own code
#assigning a list to a variable.
colors = ["Orange", "Yellow", "Green", "Pink", "Blue"]
for x in colors:
    print(x)
# passing methond for checking if something is something (in this case if x is green)
    if x == "Green":
        continue
    else:
        print ("Is that all the colors you can think of?")
