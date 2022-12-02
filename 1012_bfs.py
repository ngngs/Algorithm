import sys
from collections import deque
sys.stdin = open("C:/Users/mmm/Desktop/SWjungle/prac_python/input.txt","r")

def bfs(graph, x, y) :
    q = deque()
    q.append((x, y))
    graph[x][y] = 0
    while q :
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >=n or ny < 0 or ny >= m:
                continue
            
            if graph[nx][ny] == 1 :
                graph[nx][ny] = 0
                q.append((nx, ny))
    return
      
t = int(input())

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for _ in range(t) :
    cnt = 0
    n, m, k = map(int, sys.stdin.readline().strip().split())
    graph = [[0] * m for _ in range(n)]
    for _ in range(k) :
        x, y = map(int, sys.stdin.readline().strip().split())
        graph[x][y] = 1
    
    for i in range(n) :
        for j in range(m) :
            if graph[i][j] == 1 :
                bfs(graph, i, j)
                cnt += 1

    print(cnt)


    