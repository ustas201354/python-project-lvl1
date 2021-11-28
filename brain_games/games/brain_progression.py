#! /usr/bin/env python3

from brain_games.cli import welcome_user
from . import def_func

def main():
    name = welcome_user()
    i = 3
    while i > 0:
        i = i - 1

    # preparing example
        q = []
        q = def_func.progression()

        rigth_an = q[0]

        answer = def_func.answer()

        def_func.check_answer(answer,rigth_an,name)

if __name__ == '__main__':
    main()
