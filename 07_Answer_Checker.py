import random

# Boundaries for the numbers
low_num = 0
high_num = 20

question_num = 0

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
    input(random_item)

    # Make the equations
    subtraction_answer = (max(number_2, number_1) - min(number_1, number_2))
    addition_answer = (number_1 + number_2)
    addition_answer_v2 = (number_3 + number_2 + number_1)

    # Convert the users answer into an integer
    user_input = str(input)

    if random_item == addition_question or addition_question_v3:
        answer = addition_answer
    elif random_item == addition_question_v2:
        answer = addition_answer_v2
    else:
        answer = subtraction_answer

    print(answer)

    # Increases question number by 1
    question_num += 1
    continue