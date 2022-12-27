import sys
sys.stdin = open("C:/Users/mmm/Desktop/SWjungle/prac_python/input.txt","r")

n = int(input())
# print(n)
k = int(input())

# k번째 값보다 작은 자연수의 곱이 몇 개인지 알면 몇 번째 숫자인지 알 수 있다.

start , end = 1, k
while start <= end :
    mid = (start + end) // 2

    tmp = 0
    for i in range(1, n+1) :
        tmp += min(mid//i, n)
    if tmp >= k :
        ans = mid
        end = mid - 1
    else :
        start = mid + 1
print(ans)