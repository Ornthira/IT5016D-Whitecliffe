#I had tested the fist "Yes No Name Test" with my partner and found that I was accounting for other potential inputs, so
#amended the code to this.
#although all uppercase yes/no did not need to be included in the variables (and I know it's bad practice) because of the .lower method, 
#I wanted to include it anyway as I was still practicing assigning variables and building my own code. Also practicing "break" function.
print("Hello! Welcome to Surfers Paradise!\n")
yes = ("yes", "Yes", "y", "Y")
no = ("no", "No", "n", "N")
while True:
    name = input("What is your name?\n")
    print("Thank you,you have entered your name as", (name))
    user_answer = input("Is this correct? Please answer Yes or No:\n")
    if user_answer.lower() in yes:
        print("Great, let's continue!")
        break
    elif user_answer.lower() in no:
        print("I see.. Ok, let's try that again then.")
    else:
        user_answer = input("Sorry! I didn't quite catch that. Please type either Yes or No only\n")
        if user_answer.lower() in yes:
            print("Great, let's continue!")
            break
        elif user_answer.lower() in no:
            print("I see.. Ok, let's try that again then.")
