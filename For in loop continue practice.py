#practice code for understanding list, for loop and == 
#own code
colors = ["Orange", "Yellow", "Green", "Pink", "Blue"]
for x in colors:
    print(x)
    if x == "Green":
        continue
    else:
        print ("Is that all the colors you can think of?")
