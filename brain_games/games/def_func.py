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

def progression():
    print('What number is missing in the progression?')
    d = randint(1,5)
    a_1 = randint(1,10)
    progression = []
    len_prog = randint(1,10)
    place = randint(0,(len_prog-1))
    progression.append(a_1)

    i = 1
    while i < len_prog:
        progression.append((progression[i-1]+d))
        i += 1
    
    


#    for i in range(len_prog):
#        progression.append(randint(0,10))
    
#    print('a_1= ', a_1)
#    print('d= ', d)
#    print('len= ', len_prog)
#    print(']lace= ',place)
#    print('progression= ', progression)
    
    answer = progression[place]
#    print('answer= ',answer) 
    progression[place] = '..'
    print('Question: ', progression)

    return answer,progression

