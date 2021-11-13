#! /usr/bin/env python3

from brain_games.cli import welcome_user
from random import randint
from brain_games import def_func

name = welcome_user()
i = 3
while i > 0:
    i = i - 1

# preparing example
    q = []
    q = def_func.ran_number()

    def_func.hello_nod()
    print ('{}'.format(q[0]), '{}'.format(q[1]))

    rigth_an = def_func.gcd(q[0],q[1])

    answer = def_func.answer()

    def_func.check_answer(answer,rigth_an,name)

if __name__ == '__main__':
    main()
