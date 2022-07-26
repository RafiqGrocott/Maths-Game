from re import L


def choice_checker(add_sub_mode, sub_list, add_list, error):

    valid = False
    while not valid:

        # Ask user for choice (and put in lowercase)
        response = input(add_sub_mode).lower()

        # Iterates through list and if response us an item
        # In the list (or the first letter of an item), the
        # Full item name is returned
        for item in add_list, sub_list:
            if response == item[0] or response == item:
                return item
                
        print("item is not in list")
        print(error)
        print()

        return response

# List of acceptable expressions
sub_list = ["-", "take away", "minus", "subtraction"]
add_list = ["add", "+", "addition", "plus"]

# Ask user if they want to play addition or subtraction mode
add_sub_list = ""
while add_sub_list == "":
    add_sub_mode = choice_checker("Would you like to play the addition quiz or the subtraction quiz? Please enter + / - ", add_list, sub_list, "Please enter + or -")
    print()
    if add_sub_mode in add_list:
        print("Mode: +")
        break
    if add_sub_mode in sub_list:
        print("Mode: -")
        break
    else:
        continue