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
    
    # Increases question number by 1
    question_num += 1

    # Define addition and subtraction question
    addition_question = input("What is {} + {} =?".format(number_1, number_2))
    addition_question_v2 = input("What is {} + {} + {} =?".format(number_1, number_2, number_3))
    addition_question_v3 = input("What is {} plus {} =?".format(number_1, number_2))
    subtraction_question = input("What does {} - {} =?".format(max(number_1, number_2), min(number_1, number_2)))
    subtraction_question_v2 = input("What does {} minus {} =?".format(max(number_1, number_2), min(number_1, number_2)))

    # List of questions to randomise which question it asks
    questions = [addition_question, addition_question_v2, addition_question_v3, subtraction_question, subtraction_question_v2]

    # Randomise which question it asks
    random_item = random.choice(questions)

    # Print question
    print(random_item)