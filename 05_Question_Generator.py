import random

# Boundaries for the numbers
low_num = 0
high_num = 20

question_num = 0

while question_num <= 5:
    # Making the numbers random
    number_1 = random.randint(low_num, high_num)
    number_2 = random.randint(low_num, high_num)

    # Increases question number by 1
    question_num += 1

    # Define addition question
    addition_question = ("What is {} + {}")
    # Print the addition question
    