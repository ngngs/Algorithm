import sys
sys.stdin = open("C:/Users/mmm/Desktop/SWjungle/prac_python/input.txt","r")

n = int(input())
num = input()

sum = 0
for i in range(n) :
    sum += int(num[i])
print(sum)