import numpy as np
from collections import deque

moveX = [1, 0, -1, 0]
moveY = [0, 1, 0, -1]


def find_start(maps):
    for y in range(0, len(maps)):
        for x in range(0, len(maps[0])):
            if maps[y][x] == 'S':
                return (y, x)


def find_lever(starty, startx, maps):
    visited = [[0 for _ in range(len(maps[0]))] for _ in range(len(maps))]
    q = deque()
    q.append((starty, startx))
    visited[starty][startx] = 1
    while q:
        y, x = q.popleft()
        for d in range(0, 4):
            ny = y + moveY[d]
            nx = x + moveX[d]
            if 0 <= ny < len(maps) and 0 <= nx < len(maps[0]):
                if maps[ny][nx] != 'X' and visited[ny][nx] == 0:
                    if maps[ny][nx] == 'L':
                        return (ny, nx, visited[y][x])
                    else:
                        q.append((ny, nx))
                        visited[ny][nx] = visited[y][x] + 1
    return (-1, -1, 0)


def find_exit(levery, leverx, maps):
    visited = [[0 for _ in range(len(maps[0]))] for _ in range(len(maps))]
    q = deque()
    q.append((levery, leverx))
    visited[levery][leverx] = 1
    while q:
        y, x = q.popleft()
        for d in range(0, 4):
            ny = y + moveY[d]
            nx = x + moveX[d]
            if 0 <= ny < len(maps) and 0 <= nx < len(maps[0]):
                if maps[ny][nx] != 'X' and visited[ny][nx] == 0:
                    if maps[ny][nx] == 'E':
                        return visited[y][x]
                    else:
                        q.append((ny, nx))
                        visited[ny][nx] = visited[y][x] + 1
    return -1


def solution(maps):
    starty, startx = find_start(maps)
    levery, leverx, cost1 = find_lever(starty, startx, maps)
    if levery == -1 and leverx == -1:
        return -1
    cost2 = find_exit(levery, leverx, maps)
    if cost2 == -1:
        return -1
    return cost1 + cost2



