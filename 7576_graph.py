import sys
from collections import deque
sys.stdin = open("C:/Users/mmm/Desktop/SWjungle/prac_python/input.txt","r")

# bfs는 1인 지점에서 시작해야함
def bfs() :

    while q :
        x, y = q.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m :
                continue
            
            if graph[nx][ny] == 0 :
                graph[nx][ny] = graph[x][y] + 1
                q.append([nx, ny])
                

m, n = map(int, input().split())
# print(m, n)

# 1은 익은 토마토(ripen), 0은 익지 않은(raw), -1은 빈칸

# 최소 날짜 출력(더 이상 0 없을 때), 
# 시작부터 모두 익어있으면 0을 출력, 토마토가 익을 수 없으면 -1

dx = [1, 0 , -1, 0]
dy = [0, 1, 0, -1]

graph = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
    
# print(graph)

ans = 0
q = deque()
for i in range(n) :
    for j in range(m) :
        if graph[i][j] == 1:
            q.append([i, j])

bfs()
for i in range(n) :
    for j in range(m) :
        if graph[i][j] == 0 :
            print(-1)
            exit()
        else :
            ans = max(ans, graph[i][j])

print(ans-1)      