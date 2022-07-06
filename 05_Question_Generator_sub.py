import random

# Bondaries of the 2 numbers
low_num = 0
high_num = 20

question_num = 0


# Print 5 different questions for testing purposes
while question_num <= 4:

    # Generate a random number between boundries
    number_1 = random.randint(low_num, high_num)
    number_2 = random.randint(low_num, high_num)

    # Increases question number
    question_num += 1

    subtraction_question = ("What does {} - {} =?".format(max(number_1, number_2), min(number_1, number_2)))
    subtraction_question_v2 = ("What does {} minus {} =?".format(max(number_1, number_2), min(number_1, number_2)))
    
    # Making a list of questions to randomise
    questions = [subtraction_question, subtraction_question_v2]

    # Randomise which question it asks
    random_item = random.choice(questions)

    if number_1 >= number_2:

        print(random_item)
    else:
        print(random_item)