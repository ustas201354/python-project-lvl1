#! /usr/bin/env python3
from brain_games.cli import welcome_user
<<<<<<< HEAD
=======
from random import randint
>>>>>>> d5ddda2c73f511c39b4b3c976c59ca51d10af8df


def main():
    welcome_user()
    print ('Answer "yes" if the number is even, otherwise answer "no".')
<<<<<<< HEAD
=======
    print ('Question: ', randint(0,9))
    a = input ('Your answer: ' )
    print (a)
>>>>>>> d5ddda2c73f511c39b4b3c976c59ca51d10af8df


if __name__ == '__main__':
    main()
