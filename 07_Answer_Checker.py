import random

# Boundaries for the numbers
low_num = 0
high_num = 20

question_num = 0

# Number checking function goes here
def intcheck(question, low=None, high=None, exit_code = None):

    while True:

        #sets up error messages
        if low is not None and high is not None:
            error = "Please enter an integer between 0 and 60 (inclusive)"
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
        
# Print 5 questions for testing purposes
while question_num <= 4:

    # Making the numbers random and defining the numbers
    number_1 = random.randint(low_num, high_num)
    number_2 = random.randint(low_num, high_num)
    number_3 = random.randint(low_num, high_num)

    # Define addition question
    addition_question = ("What is {} + {} =? ".format(number_1, number_2))
    addition_question_v2 = ("What is {} + {} + {} =? ".format(number_1, number_2, number_3))
    addition_question_v3 = ("What is {} plus {} =? ".format(max(number_1, number_2), min(number_1, number_2)))

    # Define subtraction questions
    subtraction_question = ("What does {} - {} =? ".format(max(number_1, number_2), min(number_1, number_2)))
    subtraction_question_v2 = ("What does {} minus {} =? ".format(max(number_1, number_2), min(number_1, number_2)))
    
    # Making a list of questions to randomise
    questions = [subtraction_question, subtraction_question_v2, addition_question, addition_question_v2, addition_question_v3]

    # Randomise which question it asks
    random_item = random.choice(questions)

    # Letting the user input their guess
    user_input = input(random_item)

    # Make the equations
    subtraction_answer = max(number_2, number_1) - min(number_1, number_2)
    addition_answer = number_1 + number_2
    addition_answer_v2 = number_3 + number_2 + number_1

    user_input_instruction = "Guess a number between {} and {}: ".format(low_num, high_num)
    user_input = intcheck(user_input_instruction, low_num, high_num, "xxx")

    if random_item == addition_question or random_item == addition_question_v3:
        answer = addition_answer
        if user_input == answer:
            print("You got it right!!!")
        else:
            print("Oops, the answer was actually {}".format(answer))
    elif random_item == addition_question_v2:
        answer = addition_answer_v2
        if user_input == answer:
            print("You got it right!!!")
        else:
            print("Oops, the answer was actually {}".format(answer))
    else:
        answer = subtraction_answer
        if user_input == answer:
            print("You got it right!!!")
        else:
            print("Oops, the answer was actually {}".format(answer))

    # Increases question number by 1
    question_num += 1
    continue
