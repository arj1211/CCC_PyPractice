import sys

'''
Sample Input

3
2
2
-|
*+
3
5
+||*+
+++|+
**--+
2
3
+*+
+*+

Sample Output

3
7
-1
'''


# def addup(x, y):
#     top, bottom, left, right = INF, INF, INF, INF
#     if x >= 1 and grid[x - 1][y] == ('+' or '|'):
#         top = steps[x - 1][y]
#     if x < r and grid[x + 1][y] == ('+' or '|'):
#         bottom = steps[x + 1][y]
#     if y >= 1 and grid[x][y - 1] == ('+' or '-'):
#         left = steps[x][y - 1]
#     if y < c and grid[x][y + 1] == ('+' or '-'):
#         right = steps[x][y + 1]
#
#     return top, bottom, left, right

def steps_to_get_to_point(x, y):
    x = x - 1
    y = y - 1
    if grid[x - 1][y - 1] == '*':
        return INF


def BFS(x, y):
    queue = []
    visited = [[False for j in range(c + 1)] for i in range(r + 1)]
    # visited[x][y] = True
    steps[1][1] = 1
    # steps[r][c] = -1
    queue.append((x, y))
    while queue:
        print("Queue:", queue)
        current = queue.pop(0)
        print("just dequeued:", current)
        if current != (1, 1):
            steps[current[0]][current[1]] = 1 + min(steps[current[0] - 1][current[1]],
                                                    steps[current[0] + 1][current[1]],
                                                    steps[current[0]][current[1] - 1],
                                                    steps[current[0]][current[1] + 1])
        print("Steps to get to", current, ":", steps[current[0]][current[1]])
        # go to adjacent nodes
        if not visited[current[0]][current[1]]:
            visited[current[0]][current[1]] = True
            if (current[0] - 1) >= 1 and not visited[current[0] - 1][current[1]]:
                queue.append((current[0] - 1, current[1]))
            if (current[0] + 1) <= r and not visited[current[0] + 1][current[1]]:
                queue.append((current[0] + 1, current[1]))
            if (current[1] - 1) >= 1 and not visited[current[0]][current[1] - 1]:
                queue.append((current[0], current[1] - 1))
            if (current[1] + 1) <= c and not visited[current[0]][current[1] + 1]:
                queue.append((current[0], current[1] + 1))


INF = sys.maxsize

tests = int(input())  # takes in test cases

r = 0
c = 0
steps = []
grid = []

while tests > 0:  # for each test case ...
    r = int(input())  # takes in # of rows
    c = int(input())  # takes in # of cols

    grid = [['.' for j in range(c)] for i in range(r)]  # initializes character grid based on r and c vals
    for i in range(r):
        grid[i] = list(input())
        # print(grid[i])
    # grid has been inputted

    # if grid[r - 1][c - 1] == '*':
    #     steps[r][c] = -1
    #     continue

    steps = [[INF for j in range(c + 2)] for i in
             range(r + 2)]  # initializes #ofsteps grid to INF based on rows and cols (natural indexed)

    BFS(1, 1)

    print(steps[r][c])
    tests -= 1
