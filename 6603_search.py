import sys
import itertools
sys.stdin = open("C:/Users/mmm/Desktop/SWjungle/prac_python/input.txt","r")

while True :
    k, *args = map(int, sys.stdin.readline().rstrip().split())
    if k == 0 :
        exit()

    lotto_list = itertools.combinations(args, 6)
    
    for lotto in lotto_list :
        print(*lotto)

    print()