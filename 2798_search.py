import sys
import itertools

n, m = map(int, input().split())
card_list = map(int, input().split())

permu_list = itertools.combinations(card_list, 3)
min_ans = 100000000
for case in permu_list :
    ans = sum(case)
    if ans == m :
        print(ans)
        exit()
    else :
        if m-ans > 0 and m-ans < min_ans :
            min_ans = min(m-ans, min_ans)
            res = ans

print(res)