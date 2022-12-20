import sys
sys.stdin = open("C:/Users/mmm/Desktop/SWjungle/prac_python/input.txt","r")

n = input()

# if len(n) >= 4 :
#     if n[1] == 'x' :
#         res = n[2:]
#         print(int(res, 16))
#     else :
#         print(int(n))
# else :
#     if 

if n[0] == '0' :
    if n[1] == 'x' :
        res = n[2:]
        print(int(res, 16))
    else :
        print(int(n, 8))
else :
    print(int(n))