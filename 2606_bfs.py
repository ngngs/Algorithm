import sys
from collections import deque, defaultdict
sys.stdin = open("C:/Users/mmm/Desktop/SWjungle/prac_python/input.txt","r")

def bfs(n) :
    global cnt
    visited[n] = True
    q = deque([n])
    while q :
        tmp = q.popleft()
        cnt += 1
        for visit in graph[tmp] :
            if not visited[visit] :
                q.append(visit)
                visited[visit] = True

n = int(input())
m = int(input())
cnt = 0
graph = defaultdict(set)
visited = [False] * (n+1)
for _ in range(m) :
    start, end = map(int, input().strip().split())
    graph[start].add(end)
    graph[end].add(start)
# print(graph)

bfs(1)
print(cnt-1)
