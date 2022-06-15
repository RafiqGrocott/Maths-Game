def choice_checker(error, question, valid_list, addition_list, subtraction_list):

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

        return response

addition_list = ["+", "addition", "plus"]
subtraction_list = ["-", "subtraction", "take away", "minus"]

add_sub_mode = choice_checker("Would you like to play the addition game or the subtraction game? ", addition_list, subtraction_list, "Please enter '+', '-', or 'take away'")
print()