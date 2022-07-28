import random

# Lets the user enter their nmuber of rounds, or continuous mode
def check_integer(question, exit_code):
    while True:

        integer_error = "Please enter an integer " \
                        "that is more than 0\n"

        # If infinite mode not chosen, check response
        # Is an integer that is more than 0
        response = input(question)

        if response != exit_code:
            try:

                response = int(response)

                if response < 0:
                    print(integer_error)

                return response

            # If response is not an integer go back to
            # Start of loop
            except ValueError:
                print(integer_error)
                continue

        return response

question_num = 0

# Print 5 questions for testing purposes
while question_num <= 4:

    # Boundaries for the numbers
    low_num = 0
    high_num = 20

    # Making the numbers random and defining the numbers
    number_1 = random.randint(low_num, high_num)
    number_2 = random.randint(low_num, high_num)
    number_3 = random.randint(low_num, high_num)

    # Define addition question
    addition_question = ("What is {} + {} = ".format(number_1, number_2))
    addition_question_v2 = ("What is {} + {} + {} = ".format(number_1, number_2, number_3))
    addition_question_v3 = ("What is {} plus {} = ".format(number_1, number_2))

    # Define subtraction questions
    subtraction_question = ("What does {} - {} = ".format(number_2, number_1))
    subtraction_question_v2 = ("What does {} minus {} = ".format(number_2, number_1))

    # Making a list of questions to randomise
    questions = [subtraction_question, subtraction_question_v2, addition_question, addition_question_v2, addition_question_v3]

    # Randomise which question it asks
    random_item = random.choice(questions)

    # Make the equations
    subtraction_answer = number_2 - number_1
    addition_answer = number_1 + number_2
    addition_answer_v2 = number_3 + number_2 + number_1

    if random_item == addition_question or random_item == addition_question_v3:
        answer = addition_answer
    elif random_item == addition_question_v2:
        answer = addition_answer_v2
    elif random_item == subtraction_question or random_item == subtraction_question_v2:
        answer = subtraction_answer

    user_input = ""

    while user_input != answer:
        
        user_instruction = "Enter an integer higher than 0"

        end_game = "no"
        while end_game == "no":

            user_input = check_integer(random_item, "xxx")

            if user_input == answer:
                print("You got it right!!!")
            elif user_input == "xxx":
                end_game = "yes"
                break
            elif user_input == "":
                print("Please enter a valid integer!")
            else:
                print("Oops, please try again")

    # Increases question number by 1
    question_num += 1

    continue