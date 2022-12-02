import sys
import heapq

sys.stdin = open("C:/Users/mmm/Desktop/SWjungle/prac_python/input.txt","r")

n = int(input())
heap = []

for _ in range(n) :
    x = int(sys.stdin.readline().strip())
    if x != 0 :
        heapq.heappush(heap, (abs(x), x))
    
    else :
        try :
            print(heapq.heappop(heap)[1])
        except :
            print('0')
        
