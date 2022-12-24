import sys
sys.stdin = open("C:/Users/mmm/Desktop/SWjungle/prac_python/input.txt","r")

n, m = map(int, input().rstrip().split())
# print(n, m)

lecture_list = list(map(int, input().rstrip().split()))
# print(lecture_list)

max_len = max(lecture_list)
start = max_len
end = sum(lecture_list)
min_res = float("inf")

while start <= end :
    mid = (start + end) // 2
    cnt = 1
    sum_res = mid
    for num in lecture_list :
        if sum_res >= num :
            sum_res -= num
        else : 
            cnt += 1
            sum_res = mid
            sum_res -= num

        if cnt > m :
            break
        
    if cnt <= m :
        end = mid - 1
        if (mid >= max_len) :
            min_res = min(min_res, mid)
    else :
        start = mid + 1
    
    

print(min_res)
