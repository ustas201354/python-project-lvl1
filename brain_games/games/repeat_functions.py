from random import randint

def numbers():
    a = randint (0,100)
    b = randint (0,100)
    return a,b

def question():
    print ('What is the result of the expression?')

def answer():
    answer = int(input('your answer = '))
