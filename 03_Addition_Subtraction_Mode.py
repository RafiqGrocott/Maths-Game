add_sub_list = ["+", "-", "take away"]

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
        
        # Output error if item not in list
        print("item is not in list")
        print(error)
        print()

        return response

# Ask user if they want to play addition or subtraction mode
add_sub_mode = choice_checker("Would you like to play the addition game or the subtraction game? Please enter + / - ", add_sub_list, "Please enter +, -, or take away")
print()

print("Mode: ", add_sub_mode)

if add_sub_mode == "+":
    print("You chose addition mode!")

elif add_sub_mode:
    print("You chose subtraction mode!")