import sys

sys.stdin = open("C:/Users/mmm/Desktop/SWjungle/prac_python/input.txt","r")

n = int(input())
tri_list = [0] * (n+1)
# print(tri_list)
x = n
for i in range(2, n+1) :
    tri_list[i] = tri_list[i-1] + 1
    
    if i % 2 == 0 :
        tri_list[i] = min(tri_list[i], tri_list[i//2]+1)
    if i % 3 == 0 :
        tri_list[i] = min(tri_list[i], tri_list[i//3]+1)
print(tri_list[n])