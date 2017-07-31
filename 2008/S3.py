import sys

INF = sys.maxsize

tests = int(input())

while tests > 0:
    r = int(input())
    c = int(input())

    grid = [[0 for j in range(c)] for i in range(r)]
    for i in range(r):
        grid[i] = list(input())
        print(grid[i])

    steps = [[INF for j in range(c + 1)] for i in range(r + 1)]

    q = []

    tests -= 1
