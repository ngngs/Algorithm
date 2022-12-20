import sys
sys.stdin = open("C:/Users/mmm/Desktop/SWjungle/prac_python/input.txt","r")

n = int(input())
# print(n)

while n % 2 == 0 :
    n //= 2
    print(2)

i = 3
while i * i <= n :
    if n % i == 0 :
        n //= i
        print(i)
    else :
        i += 2

if n > 2 :
    print(n)