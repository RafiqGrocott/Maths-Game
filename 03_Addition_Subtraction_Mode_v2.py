from re import L

def choice_checker(add_sub_mode, list1, list2, error):

    valid = False
    while not valid:

        # Ask user for choice (and put in lowercase)
        response = input(add_sub_mode).lower()

        # Iterates through list and if response us an item
        # In the list (or the first letter of an item), the
        # Full item name is returned
        for item in list2, list1:
            if response == item[0] or response == item:
                return item

        print("item is not in list")
        print(error)
        print()

        return response


# List of acceptable expressions
sub_list = ["", "-", "take away", "minus", "subtraction"]
add_list = ["", "add", "+", "addition", "plus"]
        
# Ask user if they want to play addition or subtraction mode
add_sub_mode = choice_checker("Would you like to play the addition quiz or the subtraction quiz? Please enter + / - ", add_list, sub_list, "Please enter + or -")
print()

# Making sure the users answer is acceptable
if add_sub_mode in add_list:
    print("Mode: +")
elif add_sub_mode in sub_list:
    print("Mode: -")
while add_sub_mode != add_list or sub_list:
    continue