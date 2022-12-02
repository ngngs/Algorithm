import sys
sys.stdin = open("C:/Users/mmm/Desktop/SWjungle/prac_python/input.txt","r")

# while start <= end 일동안 진행하고
# 각 리스트 원소별 mid값으로 나눠서 몪을 CNT + 하고, MID값보다 낮으면 패스하고
# MID값에 MAX 저장하고 MAX출력하면 끝날듯?

k, n = map(int, input().split())
# print(k,n)
line_list = []
for _ in range(k) :
    line_list.append(int(sys.stdin.readline().strip()))

# print(line_list)

start = 1
end = max(line_list)
ans = float('-inf')

while start <= end :
    mid = (start + end)//2
    cnt = 0
    for i in range(k) :
        cnt += line_list[i] // mid
    # print(cnt)

    if cnt < n :
        end = mid - 1
    else :
        start = mid + 1
        ans = max(ans, mid)
print(ans)
