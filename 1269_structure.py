import sys
sys.stdin = open("C:/Users/mmm/Desktop/SWjungle/prac_python/input.txt","r")

a, b = map(int, sys.stdin.readline().rstrip().split())
# print(a, b)

a_set = set(map(int, sys.stdin.readline().rstrip().split()))
# print(a_list)
b_set = set(map(int, sys.stdin.readline().rstrip().split()))

intersection = a_set & b_set
# print(ans)

union = a_set | b_set
# print(union)

ans = union - intersection
print(len(ans))