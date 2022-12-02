import sys
from collections import deque
sys.stdin = open("C:/Users/mmm/Desktop/SWjungle/prac_python/input.txt","r")

n, k = map(int, sys.stdin.readline().rstrip().split())
# print(n, k)

q = deque()
# q.append(1)
# print(q[0])

for i in range(n) :
    q.append(i+1)

# print(q)

res = []
print('<', end = '')
while q :
    for i in range(k-1):
        tmp = q.popleft()
        q.append(tmp)
    res.append(str(q.popleft()))
print(', '.join(res), end= '')
print('>')