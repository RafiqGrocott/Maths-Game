from re import L

# List of acceptable expressions
sub_list = ["-", "take away", "minus", "subtraction"]
add_list = ["add", "+", "addition", "plus"]

# Ask user if they want to play addition or subtraction mode
add_sub_list = ""
while add_sub_list == "":
    add_sub_mode = input("Would you like to play the addition quiz or the subtraction quiz? Please enter + / - ")
    print()
    if add_sub_mode in add_list:
        print("Mode: +")
        break
    if add_sub_mode in sub_list:
        print("Mode: -")
        break
    else:
        print("Please enter a valid operation")
        continue