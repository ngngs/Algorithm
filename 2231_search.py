import sys
sys.stdin = open("C:/Users/mmm/Desktop/SWjungle/prac_python/input.txt","r")

n = input()
cnt = len(n)
ans = int(n) - (9 * cnt)

if ans < 0 :
    ans = 0

while ans != int(n) :
    check_num = ans
    for i in range(len(str(ans))) :
        check_num += int(str(ans)[i])

    if check_num == int(n) :
        print(ans)
        exit()

    else :
        ans += 1

print(0)
