import sys
from collections import deque
sys.stdin = open("C:/Users/mmm/Desktop/SWjungle/prac_python/input.txt","r")

def bfs(a, b) :
    q = deque()
    q.append((a,b))
    while q :
        x, y = q.popleft()
        for i in range(3) :
            nx = x + dx[i]
            for j in range(3) :
                ny = y + dy[j]

                if dx[i] == 0 and dx[j] == 0 :
                    continue

                if nx < 0 or ny < 0 or nx >= h or ny >= w :
                    continue

                if map_list[nx][ny] == 1 :
                    map_list[nx][ny] = 2
                    q.append((nx, ny))

while True :
    w, h = map(int, input().split())
    if w == 0 and h == 0 :
        exit()
    # print(w, h)
    map_list = []
    for _ in range(h) :
        map_list.append(list(map(int, sys.stdin.readline().strip().split())))

    # print(map_list)

    dx = [0, -1, 1]
    dy = [0, -1, 1]

    cnt = 0
    for i in range(h) :
        for j in range(w) :
            if map_list[i][j] == 1 :
                bfs(i, j)
                cnt += 1

    print(cnt)