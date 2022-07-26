import math
import random

# Show instrustions
def instructions():
    print("*****Instrustions*****")
    print()
    print("Rules of the game...")
    print()
    print("Type in the number of rounds you would like to play OR,"
                "press <enter> to play infinite mode.")
    print()
    print("Next, you will guess your number (between your high number and low number). The computer will then tell you if your guess was too high, or too low")
    print()

# checks users choice based on a list
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

# Functions go here
def check_rounds():
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


# Number checking function goes here
def intcheck(question, low=None, high=None, exit_code = None):

    while True:

        #sets up error messages
        if low is not None and high is not None:
            error = "Please enter an integer between {} and {} (inclusive)".format(low, high)
        elif low is not None and high is None:
            error = "Please enter an integer that is more than or equal to {}".format(low)
        elif low is None and high is not None:
            error = "Please enter an integer that is less than or equal to {}".format(high)
        else:
            error = "Please enter an integer"

        try:
            response = input(question)

            #check to see if response is the exit code and return it
            if response == exit_code:
                return response

            #change the response into an integer
            else:
                response = int(response)

            #checks response is not too low, not use of 'is not' keywords
            if low is not None and response < low:
                print(error)
                continue
            #checks response is not too high
            if high is not None and response > high:
                print(error)
                continue

            return response

        #checks input is a integer
        except ValueError:
            print(error)
            continue
        

# Lists of valid responses
yes_no_list = ["yes", "no"]
game_summary = []

# stores number of guesses used for each round
# used to calculate min / max / average stats
all_round_guesses = []

mode = "regular"

# ***** Main Routine *****
print("Welcome to the higher lower game")
print()

# ask user if they neeed instructions

played_before = choice_checker("Have you played this game before? Please enter yes or no. ", yes_no_list, "Please enter yes / no")
print()

if played_before == "no":
    instructions()

#ask user for number of rounds <enter> for infinite mode

# Ask user for # of rounds, <enter> for infinite mode
rounds_played = 0
rounds_won = 0
rounds_lost = 0

# ask for low number
# checks that response is a integer
low_num = intcheck("Low Number: ")
print("You chose a low number of ", low_num)


# checks for a higher number
# checks that resopnse is an integer more than the00 low number
high_num = intcheck("High Number: ", low_num + 1)
print("You chose a high number of ", high_num)

var_range = high_num - low_num + 1
max_raw = math.log2(var_range)
max_upped = math.ceil(max_raw)
max_guesses = max_upped + 1
print("Max Guesses: {}".format(max_guesses))

rounds = check_rounds()

if rounds == "":
    mode = "infinite"
    rounds = 5

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

    print(heading)

    guess = ""
    
    secret = random.randint(low_num, high_num)
    numbers_guessed = []

    print("Spoiler alert", secret)
    print()

    rounds_lost = rounds_played - rounds_won

    # guessing loop starts here
    while guess != secret and len(numbers_guessed) != max_guesses: 

        guess_instruction = "Guess a number between {} and {}: ".format(low_num, high_num)

        guess = intcheck(guess_instruction, low_num, high_num, "xxx")
        if guess == "xxx":
            end_game = "yes"
            break
        
        if guess in numbers_guessed:
            print("you already guessed this")
            continue

        if guess not in numbers_guessed:
            numbers_guessed.append(guess)

        if guess == secret:
            print("You got it!!!")
            rounds_won += 1
        

        if guess < secret:
            print("too low, guesses left {}".format(max_guesses - len(numbers_guessed)))
        elif guess > secret:
            print("too high, guesses left {}".format(max_guesses - len(numbers_guessed)))
        



        # check if they have lost
        if len(numbers_guessed) == max_guesses:
            print("Sorry you have run out of guesses")
            # rounds_lost += 1


    if len(numbers_guessed) > 0:

        all_round_guesses.append(len(numbers_guessed))


    # End game if requested # of rounds has been played

    if end_game == "yes":
        break

    rounds_played += 1

    if rounds_played == rounds:
        break

# ***** Calcuate Game stats *****

rounds_lost = rounds_played - rounds_won
percent_win = rounds_won / rounds_played * 100
percent_lose = rounds_lost / rounds_played * 100

# Displays game stats with % values to the nearest whole number
print()
print("***** Game Statistics *****")
print("Win: {}, ({:.0f}%)\nLoss: {}, ({:.0f}%)".format(rounds_won, percent_win, rounds_lost, percent_lose))
"{}".format(rounds_won, rounds_lost)
#finding smallest number

s_num = min(all_round_guesses)
s_num_max = max(all_round_guesses)
average = sum(all_round_guesses) / len(all_round_guesses)

print ()
print ("amount of guesses in each round: ", all_round_guesses)
print ("The least guesse you took were: ", s_num)
print ("The most guesses you took were: ", s_num_max)
print ("The average number of guesses you took were: {:.2f}".format(average))
print()

print()
print("Thanks for playing !!! ")