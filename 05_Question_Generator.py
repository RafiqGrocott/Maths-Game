import random

# Boundaries for the numbers
low_num = 0
high_num = 20

question_num = 0

# Print 5 questions for testing purposes
while question_num <= 5:
    # Making the numbers random and defining the numbers
    number_1 = random.randint(low_num, high_num)
    number_2 = random.randint(low_num, high_num)
    number_3 = random.randint(low_num, high_num)
    # Increases question number by 1
    question_num += 1

    # Define addition question
    addition_question = ("What is {} + {} =?".format(number_1, number_2))
    addition_question_v2 = ("What is {} + {} + {} =?".format(number_1, number_2, number_3))
    addition_question_v3 = ("What is {} plus {} =?".format(number_1, number_2))

    # List of questions to randomise which question it asks
    questions = [addition_question, addition_question_v2, addition_question_v3]

    # Randomise which question it asks
    random_item = random.choice(questions)

    # Print question
    print(random_item)