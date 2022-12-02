import sys
from collections import deque
sys.stdin = open("C:/Users/mmm/Desktop/SWjungle/prac_python/input.txt","r")


def bfs(n) :
    q = deque()
    q.append(n)
    while q :
        tmp = q.popleft()
        if tmp == k :
            print(graph[tmp])
            exit()

        for nx in (tmp-1, tmp+1, tmp*2) :
            if 0 > nx or MAX < nx :
                continue

            if not graph[nx] :
                graph[nx] = graph[tmp] + 1
                q.append(nx)

n, k = map(int, sys.stdin.readline().strip().split())
# print(n, k)

MAX = 10 ** 5
graph = [0] * (MAX+1)
# print(graph)

bfs(n)