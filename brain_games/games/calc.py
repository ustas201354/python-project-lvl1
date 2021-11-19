#! /usr/bin/env python3
from brain_games.cli import welcome_user
from random import randint

def main():
    name = welcome_user()
    i = 3
    while i > 0:
        i = i - 1

    # preparing example
        a = randint (0,10)
        b = randint (0,10)

        #choose the sign
        lst = ['+','-','*']
        ran = randint(0,2)
        sign = lst[ran]
        #print ('sign ', sign

        print ('What is the result of the expression?')
        print ('{}'.format(a), '{}'.format(sign), '{}'.format(b))

        if sign == '+':
            rigth_an = a + b
        elif sign == '-':
            rigth_an = a - b
        else:
            rigth_an = a * b

        #print ('right answer = ', rigth_an)
        #print (type(rigth_an))


        answer = int(input ('your answer = '))
        #print (type(answer))

        if answer == rigth_an:
            print ('Correct!!!')
        else:
            print ('{}'.format(answer), 'is wrong answer ;(. Correct answer was {}'.format(rigth_an), 'Lets try again {}'.format(name))
            break
if __name__ == '__main__':
    main()
