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
