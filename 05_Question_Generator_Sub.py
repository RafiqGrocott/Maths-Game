import random

# Bondaries of the 2 numbers
low_num = 0
high_num = 20

question_num = 0

# Print 5 different questions for testing purposes
while question_num <= 5:
    # Generate a random number between boundries
    number_1 = random.randint(low_num, high_num)
    number_2 = random.randint(low_num, high_num)

    # Increases question number
    question_num += 1

    # Make sure the question doesn't go into the negatives
    if number_1 >= number_2:
        subtraction_question = ("What does {} - {} =?".format(number_1, number_2))
    else:
        subtraction_question = ("What does {} - {} =?".format(number_2, number_1))

    print(subtraction_question)