#! /usr/bin/env python3
from brain_games.cli import welcome_user
from random import randint


def main():
    welcome_user()
    print ('Answer "yes" if the number is even, otherwise answer "no".')
    print ('Question: ', randint(0,9))
    a = input ('Your answer: ' )
    print (a)


if __name__ == '__main__':
    main()
