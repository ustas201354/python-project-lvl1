#! /usr/bin/env python3
from brain_games.cli import welcome_user
from random import randint


def main():
    welcome_user()
    b = randint(0,9)
    y = ''
    n = ''
    if b % 2 == 0:
        print ('Even number')
        y == 'yes'
    else:
        print ('Uneven number')
        n == 'no'

    print ('Answer "yes" if the number is even, otherwise answer "no".')
    print ('Question: ', b)
    a = input ('Your answer: ' )

    if a == y or a == n:
        print ('Congratulations!!!')


if __name__ == '__main__':
    main()
