import sys
sys.stdin = open("C:/Users/mmm/Desktop/SWjungle/prac_python/input.txt","r")

arr = list(map(int, sys.stdin.readline().rstrip()))
arr.sort(reverse=True)
# print(arr)
print(*arr, sep='')