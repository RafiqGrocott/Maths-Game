import random

# Boundaries for the numbers
low_num = 0
high_num = 20

question_num = 0

# Making the numbers random
number_1 = random.randint(low_num, high_num)
number_2 = random.randint(low_num, high_num)

# Generate questions with the random numbers
addition_question = input("What does {} + {} =? ".format(number_1, number_2))

print("Question {}".format(question_num))

# Printing question
user_answer = int(addition_question)

# Answer to the question
addition_answer = number_1 + number_2

while question_num <= 5:
    print("Question {}".format(question_num))
    question_num += 1
    addition_question = input("What does {} + {} =? ".format(number_1, number_2))
    while user_answer == addition_answer:
        print("You got it right!!!")
        break
    else:
        print("Oops, the answer was actually {}.".format(addition_answer))
    # Gap between feeback and next question
    print()