import random

# Bondaries of the 2 numbers
low_num = 0
high_num = 20

question_num = 0

while question_num <= 5:
    # Generate a random number between boundries
    number_1 = random.randint(low_num, high_num)
    number_2 = random.randint(low_num, high_num)
    question_num += 1
    if number_1 >= number_2:
        subtraction_question = ("What does {} - {} =?".format(number_1, number_2))
    else:
        subtraction_question = ("What does {} - {} =?".format(number_2, number_1))

    print(subtraction_question)



