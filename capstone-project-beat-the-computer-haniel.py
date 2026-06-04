#capstone-project-beat-the-computer.py
#import liberias
import random
from time import time
score=0
time_limit=10
#greeting user
#over
def greet_user():
    name=input("Enter your name:")
    print(f"{name} Welcome to beat computer in Maths Game")
#operation generator
#over
def operations_generator():
    operations = ["+", "-", "*", "/"]
    operation = random.choice(operations)
    return operation
#input_generator
#over
def input_generator():
    a=random.randint(1,10)
    b=random.randint(1,10)
    return a,b
#display_question
#over
def display_question(a,operations,b):
    print("Try to solve" ,a,operations,b)
#start_timer
#over
def start_timer():
    start_time = time()
    print(f"you have {time_limit} seconds !!! Your time starts now")
    return start_time
#get_answer
#over
def get_answer():
    user_answer=int(input("enter the answer to the question:"))
    return user_answer
#timer_core
def timer_core(ime_limit,time_taken):
    start_timer()
#answer_generator
#over
def answer_generator(a,operations,b):
    if operations =="+":
        correct_answer=a+b
    elif operations=="-":
        correct_answer=a-b
    elif operations == "*":
        correct_answer = a*b
    elif operations=="/":
        correct_answer=a/b
#verify_answer
#over
def verify_answer(correct_answer,answer,user_answer):
    if answer==correct_answer:
        print(f"{user_answer} correct answer you get a point")
    else:
        print(f"incorrect answer the correct answer{correct_answer}")
#score_generator
#over
def score_generator(correct_answer,answer):
    if answer==correct_answer:
        score=+1
    else:
        pass
def play(user_answer,correct_answer,answer,a,operation,b):
    greet_user()
    operation=operations_generator()
    a,b=input_generator()
    display_question(a,operation,b)
    start_timer()
    get_answer()
    answer_generator(a,operation,b)
    verify_answer(correct_answer=int,answer=int,user_answer=int)
    score_generator(correct_answer=int,answer=int)
play(user_answer=int,correct_answer=int,answer=int,a=int,operation=str,b=int)
