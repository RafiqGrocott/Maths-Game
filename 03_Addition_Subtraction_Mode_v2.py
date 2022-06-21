def choice_checker(question, add_sub_list, error):

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
                
        print("item is not in list")
        print(error)
        print()

        return response

add_sub_list = ["+", "-", "take away", "minus", "plus", "subtract", "add"]

# Ask user if they want to play addition or subtraction mode
add_sub_mode = choice_checker("Would you like to play the addition game or the subtraction game? Please enter + / - ", add_sub_list, "Please enter +, -, or take away")
print()

print("Mode: ", add_sub_mode)

if add_sub_mode == "+" "Addition" "Add" "Plus":
    print("You chose addition mode!")

if add_sub_mode == "-" "minus" "subtract" "subtract":
    print("You chose subtraction mode!")

else:
    print(error)