import random

# Boundaries for the numbers
low_num = 0
high_num = 20

question_num = 0

while question_num < 4:
    # Making the numbers random and defining the numbers
    number_1 = random.randint(low_num, high_num)
    number_2 = random.randint(low_num, high_num)
    number_3 = random.randint(low_num, high_num)

    # Define subtraction questions
    subtraction_question = input("What does {} - {} =? ".format(max(number_1, number_2), min(number_1, number_2)))
    subtraction_question_v2 = input("What does {} minus {} =? ".format(max(number_1, number_2), min(number_1, number_2)))

    question_num += 1