#!/usr/bin/python3
""" n-queens puzzle """
import sys


def chess(n):
    """ chessboard of size n """
    floor = []
    [floor.append([]) for i in range(n)]
    [m_r.append(' ') for i in range(n) for m_r in floor]
    return (floor)


def another_board(chessboard):
    """ return identical chessboard """
    if isinstance(chessboard, list):
        return list(map(another_board, chessboard))
    return (chessboard)


def solved(chessboard):
    """ returns the solved chessboard """
    sol = []
    for x in range(len(chessboard)):
        for y in range(len(chessboard)):
            if chessboard[x][y] == "Q":
                sol.append([x, y])
                break
    return (sol)


def stopx(chessboard, col, row):
    """ places where fallen queens are obselete """
    for y in range(col + 1, len(chessboard)):
        chessboard[row][y] = "x"
    for y in range(col - 1, -1, -1):
        chessboard[row][y] = "x"
    for x in range(row + 1, len(chessboard)):
        chessboard[x][col] = "x"
    for x in range(row - 1, -1, -1):
        chessboard[x][col] = "x"
    y = col + 1
    for x in range(row + 1, len(chessboard)):
        if y >= len(chessboard):
            break
        chessboard[x][y] = "x"
        y += 1
    y = col - 1
    for x in range(row - 1, -1, -1):
        if y < 0:
            break
        chessboard[x][y]
        y -= 1
    y = col + 1
    for x in range(row - 1, -1, -1):
        if y >= len(chessboard):
            break
        chessboard[x][y] = "x"
        y += 1
    y = col - 1
    for x in range(row + 1, len(chessboard)):
        if y < 0:
            break
        chessboard[x][y] = "x"
        y -= 1


def fullsolve(chessboard, row, gis, sol):
    """ solves the n-queen puzzle """
    if gis == len(chessboard):
        sol.append(solved(chessboard))
        return (sol)
    for y in range(len(chessboard)):
        if chessboard[row][x] == " ":
            my_board = another_board(chessboard)
            my_board[row][c] = "Q"
            stopx(my_board, row, y)
            sol = fullsolve(my_board, row + 1, gis + 1, sol)
    return (sol)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)
    chessboard = chess(int(sys.argv[1]))
    sol = fullsolve(chessboard, 0, 0, [])
    for so in sol:
        print(so)
