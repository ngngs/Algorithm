import sys
from collections import deque
sys.stdin = open("C:/Users/mmm/Desktop/SWjungle/prac_python/input.txt","r")

n = int(input())
# print(n)

visit = [[-1] * (n+1) for _ in range(n+1)]
q = deque()
q.append((1,0)) # 화면 이모티콘, 클립보드 이모티콘
visit[1][0] = 0
while q :
    s,c = q.popleft()
    if visit[s][s] == -1 :
        visit[s][s] = visit[s][c] + 1
        q.append((s,s))
    if s+c <= n and visit[s+c][c] == - 1:
        visit[s+c][c] = visit[s][c] + 1
        q.append((s+c, c))
    if s-1 >= 0 and visit[s-1][c] == -1:
        visit[s-1][c] = visit[s][c] + 1
        q.append((s-1, c))
ans = -1
for i in range(n+1) :
    if visit[n][i] != -1 :
        if ans == -1 or ans > visit[n][i] :
            ans = visit[n][i]
print(ans)

