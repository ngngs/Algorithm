import sys
sys.stdin = open("C:/Users/mmm/Desktop/SWjungle/prac_python/input.txt","r")

n, m = map(int, input().split())
# print(n, m)

a_list = list(map(int, sys.stdin.readline().rstrip().split()))
# print(a_list)
b_list = list(map(int, sys.stdin.readline().rstrip().split()))
# print(b_list)

a_list.extend(b_list)
a_list.sort()
print(*a_list)