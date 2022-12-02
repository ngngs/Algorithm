import sys
from collections import deque
sys.stdin = open("C:/Users/mmm/Desktop/SWjungle/prac_python/input.txt","r")

def dfs(n) :
    visited1[n] = True
    res.append(n)
    # print(n, end= " ")
    for i in node_list[n] :
        if visited1[i] == False :
            dfs(i)
            
def bfs(n) :
    visited2[n] = True
    q = deque()
    q.append(n)
    while q :
        tmp = q.popleft()
        res2.append(tmp)
        # print(tmp, end= ' ')
        for i in node_list[tmp] :
            if visited2[i] == False :
                q.append(i)
                visited2[i] = True

n, m, v = map(int, sys.stdin.readline().strip().split())
# print(n,m,v)

node_list = [[] for _ in range(n+1)]
visited1 = [False for _ in range(n+1)]
visited2 = [False for _ in range(n+1)]
# print(visited)
# print(visited)
for _ in range(m) :
    start, end = map(int, sys.stdin.readline().strip().split())
    node_list[start].append(end)
    node_list[end].append(start)

for i in range(1, n+1) :
    node_list[i].sort()
print(node_list)

res = []
res2 = []
dfs(v)
print(*res)
bfs(v)
print(*res2)