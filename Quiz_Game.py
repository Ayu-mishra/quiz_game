
import time

questions = [
    {
        "question" : "Which language is used for web apps?",
        "options" : ["A. Python", "B. Java", "C. Javascript", "D. C++"],
        "answer" : "C"
    },
    {
        "question" : "What is the capital of france?",
        "options" : ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
        "answer" : "C"
    },
    {
        "question" : "Who developed python? ",
        "options" : ["A. James Gosling", "B. Guido van Rossum", "C. Elon musk", "D. Rock"],
        "answer" : "B"
    },
    {
        "question" : "Which keyword is used to create a function in Python? ",
        "options" : ["A. func", "B. def", "C. function", "D. create"],
        "answer" : "B"
    },
    {
        "question" :"Which year was Python released?",
        "options" : ["A. 1991", "B. 1985", "C. 2000", "D. 2022"],
        "answer" : "A"
    }
]

score = 0
time_limit = 10

print ("\nWelcome to the quiz game")
print("You have 10 seconds to answer each question.\n")

for i, q in enumerate(questions, start=1):
    print(f"Q{i}: {q['question']}")
    for opt in q['options']:
        print(opt)

    start_time = time.time()
    answer = input("Your Answer (A/B/C/D):").upper()
    end_time = time.time()

    if (end_time - start_time) > time_limit:
        print("Time's up! No points for this question.\n")
        continue 

    if answer == q['answer']:
        print("Correct\n")
        score += 1

    else :
        print(f"Wrong correct answer is {q ['answer']}.\n")
        continue

print(f"Your final score : {score}/{len(questions)}")
print("")
print("Thanks for playing")
print("")
print("Have a good day!!")