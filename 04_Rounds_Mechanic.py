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

        print(heading)

    if end_game == "yes":
        break

    rounds_played += 1

    if rounds_played >= rounds:
        break