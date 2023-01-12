import sys
sys.stdin = open("C:/Users/mmm/Desktop/SWjungle/prac_python/input.txt","r")

n = int(input())
# print(n)
tri_list = []
for _ in range(n) :
    tri_list.append(list(map(int, input().split())))
# print(tri_list)


k = 2
for i in range(1, n) :
    for j in range(k) :
        if j == 0 :
            tri_list[i][j] = tri_list[i][j] + tri_list[i-1][j]
        elif i == j :
            tri_list[i][j] = tri_list[i][j] + tri_list[i-1][j-1]
        else :
            tri_list[i][j] = max(tri_list[i-1][j-1], tri_list[i-1][j]) + tri_list[i][j]
    k += 1

print(max(tri_list[n-1]))