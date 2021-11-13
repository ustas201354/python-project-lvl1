from random import randint

def ran_number():
    a = randint (0,100)
    b = randint (0,100)
    return a,b

def hello():
    print ('What is the result of the expression?')

def hello_nod():
    print ('Find the greatest common divisor of given numbers.')

def answer():
    answer = int(input ('your answer = '))
    return answer

def check_answer(answer, rigth_an, name):
    if answer == rigth_an:
        print ('Correct!!!')
    else:
        print ('{}'.format(answer), 'is wrong answer ;(. Correct answer was {}'.format(rigth_an), 'Lets try again {}'.format(name))

def gcd(a,b):
    while a != 0 and b != 0:
        if a >= b:
            a %= b
        else:
            b %= a
    return a or b

