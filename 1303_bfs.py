import sys
from collections import deque
sys.stdin = open("C:/Users/mmm/Desktop/SWjungle/prac_python/input.txt","r")

def bfs(x,y, color) :
    cnt = 1
    q=deque([[x,y]])
    visited[x][y] = True
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    while q :
        nx, ny = q.popleft()

        for i in range(4) :
            tmp_x = nx + dx[i]
            tmp_y = ny + dy[i]

            if tmp_x < 0 or tmp_y < 0 or tmp_x > m-1 or tmp_y > n-1 :
                continue

            if graph[tmp_x][tmp_y] == color and visited[tmp_x][tmp_y] == False  :
                q.append([tmp_x, tmp_y])
                visited[tmp_x][tmp_y] = True
                cnt += 1
    return cnt

n, m = map(int, input().rstrip().split())
white_cnt = 0
blue_cnt = 0
graph = []
visited = [[False] * n for _ in range(m)]
for i in range(m) :
    graph.append(list(sys.stdin.readline().rstrip()))


for i in range(m) :
    for j in range(n) :
        if visited[i][j] == False and graph[i][j] == 'W' :
            white_cnt += bfs(i, j, 'W') ** 2
        elif visited[i][j] == False and graph[i][j] == 'B' :
            blue_cnt += bfs(i, j, 'B') ** 2


print(white_cnt, blue_cnt)
