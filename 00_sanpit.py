# Lets the user enter their nmuber of rounds, or continuous mode
def check_integer():
    while True:
        response = input("How many rounds? or <enter> for continuous mode: ")
        print()


        integer_error = "Please enter an integer " \
                        "that is more than 0\n"

        # If infinite mode not chosen, check response
        # Is an integer that is more than 0
        if response != "":
            try:
                response = int(response)

                # If response is too low, go back to
                # Start of loop
                if response < 1:
                    print(integer_error)
                    continue
            # If response is not an integer go back to
            # Start of loop
            except ValueError:
                print(integer_error)
                continue

        return response