import sys
sys.stdin = open("C:/Users/mmm/Desktop/SWjungle/prac_python/input.txt","r")

n = int(input())
sangeun_list = list(map(int, sys.stdin.readline().split()))
sangeun_list.sort()

m = int(input())
check_list = list(map(int, sys.stdin.readline().split()))

res = []
for target in check_list :
    start = 0
    end = len(sangeun_list)-1
    flag = False
    while start <= end :
        mid = (start + end) // 2

        if target == sangeun_list[mid] :
            res.append(1)
            flag = True
            break
        elif target < sangeun_list[mid] :
            end = mid - 1
        else :
            start = mid + 1
    if flag == False :
        res.append(0)


print(*res)
    