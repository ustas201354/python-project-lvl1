#! /usr/bin/env python3
from brain_games.cli import welcome_user
from random import randint


def main():
    welcome_user()
    print ('Answer "yes" if the number is even, otherwise answer "no".')
   
    i = 3
    while i > 0:
        i = i-1
        print ('i = ', i)
    


        b = randint(0,1000)
        y = ''
        n = ''
        if b % 2 == 0:
            print ('Even number')
            y = 'yes'
            print (y)
        else:
            print ('Uneven number')
            n = 'no'
            print (n)

        print ('Question: ', b)
        a = input ('Your answer: ' )
        if a == y or a == n:
            print ('Congratulations!!!')
        else:
            print ('Unncorrect input, print yes or no')


if __name__ == '__main__':
    main()
