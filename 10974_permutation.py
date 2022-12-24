import sys
import itertools
sys.stdin = open("C:/Users/mmm/Desktop/SWjungle/prac_python/input.txt","r")

n = int(input())

fact_list = []
for i in range(n) :
    fact_list.append(i+1)

factorial = itertools.permutations(fact_list,n)

for ans in factorial :
    print(*ans)

