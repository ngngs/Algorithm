import sys

sys.stdin = open("C:/Users/mmm/Desktop/SWjungle/prac_python/input.txt","r")

n, m, k = list(map(int, sys.stdin.readline().split()))
# print(n, m, k)

if n == m == k :
    print(10000 + (n * 1000))

elif n == m and n != k and m != k :
    print(1000 + (n * 100))
elif n == k and n != m and m != k :
    print(1000 + (n * 100))
elif m == k and n != m and n != k :
    print(1000 + (m * 100))

else :
    ans = max(n, m, k)
    print(ans * 100)