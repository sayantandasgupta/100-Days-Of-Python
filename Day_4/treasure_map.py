'''
Exercise 3 for Day 4 of 100 Days of Python

For this exercise we are going to mark the spot X on a 2D grid of size 3 by 3

The grid is composed of a list of lists. Initially it will be like the following:-

[
    ['⬜️', '⬜️', '⬜️'],
    ['⬜️', '⬜️', '⬜️'],
    ['⬜️', '⬜️', '⬜️']
]

Given a number as input, say 31, we have to mark X on column 3 and row 1, considering that in Python lists, index begins from 0

For input 31, output:-

[
    ['⬜️', '⬜️', 'X'],
    ['⬜️', '⬜️', '⬜️'],
    ['⬜️', '⬜️', '⬜️']
]
'''


def mark(pos):
    map = [
        ['⬜️', '⬜️', '⬜️'],
        ['⬜️', '⬜️', '⬜️'],
        ['⬜️', '⬜️', '⬜️']
    ]

    x = (pos % 10) - 1
    y = (pos // 10) - 1

    map[x][y] = 'X'

    display(map)


def display(grid):
    for i in grid:
        for j in i:
            print(j, end=' ')
        print()


if __name__ == "__main__":
    position = int(
        input("Enter the position at which the treasure should be hidden: "))

    mark(position)
