#one of my first practice codes playing around with assigning variables and understanding while true loops - if, elif and else.
#inspiration taken from reading online materials on "Geeksforgeeks" website https://www.geeksforgeeks.org/python-programming-language/
print("Hello world\n")
yes = ("yes" , "Yes")
no =("no", "No")
while True:
    name = input("What is your name?")
    print("Thank you,you have input your name as", (name))
    user_answer = input("Is this correct? Please answer Yes or No: ")
    if user_answer.lower() in yes :
        print("Great, let's continue!")
        break
    elif user_answer.lower() in no:
        print("Please enter your the correct name")
    else:
        print("Please type either yes or no only")
