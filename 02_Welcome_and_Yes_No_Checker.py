print("***** Welcome to THE MATHS GAME *****")
print()

# checks users choice based on a list

def instructions():
    print("*****Instrustions*****")
    print()
    print("Rules of the game...")
    print()
    print("You will be asked addition and subtraction questions.")
    print()
    print("As you go along, the code will calculate the number of rounds you've won and lost"
        "and will eventually tell you how many you won and lost, and also the percentage of rounds you won and lost.")
    print()
    print("Won = Answered question correctly. ")
    print()
    print("Lost = Answered question incorrectly.")


def choice_checker (question, valid_list, error):

    valid = False
    while not valid:

        # Ask user for choice (and put in lowercase)
        response = input(question).lower()

        # Iterates through list and if response us an item
        # In the list (or the first letter of an item), the
        # Full item name is returned
        for item in valid_list:
            if response == item[0] or response == item:
                return item
        
        # Output error if item not in list
        print("item is not in list")
        print(error)
        print()

yes_no_list = ["yes", "no"]

played_before = choice_checker("Have you played this game before? Please enter yes or no. ", yes_no_list, "Please enter yes / no")
print()

if played_before == "no":
    instructions()