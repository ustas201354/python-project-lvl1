#! /usr/bin/env python3
from brain_games.cli import welcome_user
from random import randint


def main():
    name =  welcome_user()
    print ('Answer "yes" if the number is even, otherwise answer "no".')
   
    i = 3
    while i > 0:
        i = i-1

        b = randint(0,1000)
        y = ''      
        if b % 2 == 0:
            y = 'yes'
        else:
            y = 'no'
            
        print ('Question: ', b)
        a = input ('Your answer: ' )
        if a == y:
            print ('Congratulations!!!')
        else:
            print ( a , 'is wrong answer ;(. Correct answer was', y,
                    'Lets try again', name)


if __name__ == '__main__':
    main()
