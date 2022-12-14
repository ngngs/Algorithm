import sys
sys.stdin = open("C:/Users/mmm/Desktop/SWjungle/prac_python/input.txt","r")

sugar_wt = int(input())
# print(sugar)

k = sugar_wt // 5
while k != -1 :
    if k != 0 :
        sugar_five_minus = sugar_wt - (5 * k)
        if sugar_five_minus % 3 == 0 :
            ans = k + (sugar_five_minus // 3)
            print(ans)
            exit()
        else :
            k -= 1
    else :
        if sugar_wt % 3 == 0 :
            print(sugar_wt // 3)
            exit()
        else :
            k -= 1
        
print(-1)

