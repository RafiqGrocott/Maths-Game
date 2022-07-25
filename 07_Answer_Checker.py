import random

def intcheck(response, num_high, num_low):
    if response >= num_high or response <= num_low:
        print("Please enter an integer which is between 0 and 61 (inclusive)")
    try:
        print(response)

        if response == exit_code:
            return response
        
        else: response = int(response)

    except ValueError:
        print("Please enter an integer which is between 0 and 61 (inclusive)")
    
# Make sure the users answer is between 0 and 60 (inclusive)
num_high = 61
num_low = -1

# Define what the exit code is
exit_code = "xxx"

# Make question number
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
    addition_question = ("What is {} + {} =? ".format(number_1, number_2))
    addition_question_v2 = ("What is {} + {} + {} =? ".format(number_1, number_2, number_3))
    addition_question_v3 = ("What is {} plus {} =? ".format(number_1, number_2, number_3))

    # Define subtraction questions
    subtraction_question = ("What does {} - {} =? ".format(number_1, number_2))
    subtraction_question_v2 = ("What does {} minus {} =? ".format(number_1, number_2))
    
    # Making a list of questions to randomise
    questions = [subtraction_question, subtraction_question_v2, addition_question, addition_question_v2, addition_question_v3]

    # Randomise which question it asks
    random_item = random.choice(questions)

    if random_item == subtraction_question or random_item == subtraction_question_v2:
        number_2 > number_1

    addition_answer = number_1 + number_2
    addition_answer_v2 = number_1 + number_2 + number_3
    subtraction_answer = number_1 - number_2

    if random_item == addition_question or random_item == addition_question_v3:
        answer = addition_answer
    elif random_item == subtraction_question or random_item == subtraction_question_v2:
        answer = subtraction_answer
    else:
        answer = addition_answer_v2

    response = input(random_item)

    if response == answer:
        print("You got it right")
    elif response == "":
        print("Please enter a valid answer")

    # Add one more round onto the question_num
    question_num += 1