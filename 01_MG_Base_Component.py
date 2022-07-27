import random
from re import L
from tkinter import Y

# Welcomes user to game
print("***** Welcome to THE MATHS GAME *****")
print()

# Prints instructions if user enters "no" in played_before
def instructions():
    print("*****Instrustions*****")
    print()
    print("Rules of the game...")
    print()
    print("You will be asked addition and subtraction questions.")
    print()
    print()
    print("As you go along, the code will calculate the number of rounds you've won and lost"
        "and will eventually tell you how many you won and lost, and also the percentage of rounds you won and lost.")
    print()
    print("Won = Answered question correctly. ")
    print()
    print("Lost = Answered question incorrectly.")
    print()

# Checks if the users choice is valid for add_sub_mode
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

# Lets the user enter their nmuber of rounds, or continuous mode
def check_integer():
    while True:
        response = input("How many rounds? or <enter> for continuous mode: ")
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

# List of acceptable expressions
sub_list = ["-", "take away", "minus", "subtraction"]
add_list = ["add", "+", "addition", "plus"]

# Boundaries for the numbers
low_num = 0
high_num = 20

# Gives a clean slate to add to and eventually make end of game statements on
rounds_played = 0
rounds_lost = 0
rounds_won = 0

# Check if the user has played this game before
played_before = choice_checker("Have you played this game before? Please enter yes or no. ", yes_no_list, "Please enter yes / no")
print()

# If the user hasn't played before they get to see the instructions
if played_before == "no":
    instructions()

# Ask user if they want to play addition or subtraction mode
add_sub_list = ""
while add_sub_list == "":
    add_sub_mode = input("Would you like to play the addition quiz or the subtraction quiz? Please enter + / - ")

    print()

    if add_sub_mode in add_list:
        game_mode = "+"
        print("Mode: +")
        break
    if add_sub_mode in sub_list:
        game_mode = "-"
        print("Mode: -")
        break
    else:
        print("Please enter a valid operation")
        continue

mode = "regular"

rounds_played = 0
rounds = check_integer()

# If the user presses <enter> then run infinite mode
if rounds == "":
    mode = "infinite"
    rounds = 5

end_game = "no"
while end_game == "no":

    # Rounds Heading
    print()
    if mode == "infinite":
        heading = "Continuous Mode: Round {}".format(rounds_played + 1)
        rounds += 1
    else:
        heading = "Round {} of {}".format(rounds_played + 1, rounds)
    
    print(heading)

    # Increases round number
    rounds_played += 1

    # Generate a random number between boundries
    number_1 = random.randint(low_num, high_num)
    number_2 = random.randint(low_num, high_num)
    number_3 = random.randint(low_num, high_num)

    # Define addition and subtraction question
    addition_question = ("What is {} + {} =? ".format(number_1, number_2))
    addition_question_v2 = ("What is {} + {} + {} =? ".format(number_1, number_2, number_3))
    addition_question_v3 = ("What is {} plus {} =? ".format(number_1, number_2))
    subtraction_question = ("What does {} - {} =? ".format(max(number_1, number_2), min(number_1, number_2)))
    subtraction_question_v2 = ("What does {} minus {} =? ".format(max(number_1, number_2), min(number_1, number_2)))
                        
    # List of questions to randomise which question it asks
    questions = [addition_question, addition_question_v2, addition_question_v3, subtraction_question, subtraction_question_v2]
    addition_questions = [addition_question, addition_question_v2, addition_question_v3]
    subtraction_questions = [subtraction_question, subtraction_question_v2]

    # Making a list of questions to randomise
    questions = [subtraction_question, subtraction_question_v2, addition_question, addition_question_v2, addition_question_v3]

    # Make sure the different modes of the game work
    add_question = random.choice(addition_questions)
    sub_question = random.choice(subtraction_questions)

    # If the game mode is addition mode then only print addition questions
    if game_mode == "+":
        print(input(add_question))
    # If the game mode is subtraction mode then only print subtraction questions
    else:
        print(input(sub_question))

    # Randomise which question it asks
    random_item = random.choice(questions)

    if random_item == subtraction_question or random_item == subtraction_question_v2:
        number_2 > number_1

    addition_answer = number_1 + number_2
    addition_answer_v2 = number_1 + number_2 + number_3
    subtraction_answer = number_1 - number_2

    if random_item == addition_question or random_item == addition_question_v3:
        answer = addition_answer
    elif random_item == subtraction_question or random_item == subtraction_question_v2:
        answer = subtraction_answer
    else:
        answer = addition_answer_v2

    response = input(random_item)

    if response == answer:
        print("You got it right")
    elif response == "":
        print("Please enter a valid answer")

    if rounds_played >= rounds:
        break