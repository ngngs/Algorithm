import sys

sys.stdin = open("C:/Users/mmm/Desktop/SWjungle/prac_python/input.txt","r")

n, m = list(map(int, sys.stdin.readline().split()))
# print(n, m)

unseen_list = set()
unlisten_list = set()
for i in range(n) :
    unseen_list.add(sys.stdin.readline().rstrip())
# print(unseen_list)
for j in range(m) :
    unlisten_list.add(sys.stdin.readline().rstrip())
# print(unlisten_list)

ans = sorted(list(unseen_list & unlisten_list))
print(len(ans))

for i in ans :
    print(i)