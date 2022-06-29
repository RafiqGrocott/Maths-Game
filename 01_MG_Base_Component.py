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
    print("Cargan was here 8----")
    print()
    print("As you go along, the code will calculate the number of rounds you've won and lost"
        "and will eventually tell you how many you won and lost, and also the percentage of rounds you won and lost.")
    print()
    print("Won = Answered question correctly. ")
    print()
    print("Lost = Answered question incorrectly.")
    print()


def choice_checker (question, add_sub_list, error):

    valid = False
    while not valid:

        # Ask user for choice (and put in lowercase)
        response = input(question).lower()

        # Iterates through list and if response us an item
        # In the list (or the first letter of an item), the
        # Full item name is returned
        for item in add_sub_list:
            if response == item[0] or response == item:
                return item
        
        # Output error if item not in list
        print("item is not in list")
        print(error)
        print()

def check_rounds():
    while True:
        response = input("How many questions? or <enter> for continuous mode: ")
        print()


        round_error = "Please type either <enter> or an integer " \
                        "that is more than 0\n"

        # If infinite mode not chosen, check response
        # Is an integer that is more than 0
        if response != "":
            try:
                response = int(response)

                # If response is too low, go back to
                # Start of loop
                if response < 1:
                    print(round_error)
                    continue
            # If response is not an integer go back to
            # Start of loop
            except ValueError:
                print(round_error)
                continue

        return response



# List of acceptable expressions
yes_no_list = ["yes", "no"]

played_before = choice_checker("Have you played this game before? Please enter yes or no. ", yes_no_list, "Please enter yes / no")
print()

if played_before == "no":
    instructions()

mode = "regular"
rounds = check_rounds()

if rounds == "":
    mode = "infinite"
    rounds = 5

rounds_played = 0
rounds_lost = 0
rounds_won = 0

# game loop starts here
end_game = "no"
while end_game == "no":

    # Rounds Heading
    print()
    if mode == "infinite":
        heading = "Continuous Mode: Round {}".format(rounds_played + 1)
        rounds += 1

    else:
        heading = "Round {} of {}".format(rounds_played + 1, rounds)

    
    # Rounds Heading
    print()
    if mode == "infinite":
        heading = "Continuous Mode: Question {}".format(rounds_played + 1)
        rounds += 1

    else:
        heading = "Question {} of {}".format(rounds_played + 1, rounds)

        print(heading)

    if end_game == "yes":
        break

    rounds_played += 1

    if rounds_played >= rounds:
        break