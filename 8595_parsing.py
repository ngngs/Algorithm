import sys
import re
sys.stdin = open("C:/Users/mmm/Desktop/SWjungle/prac_python/input.txt","r")

n = int(input())
# print(n)

input_val = sys.stdin.readline().rstrip()

num_list = re.findall('\d+', input_val)
ans = 0
for hidden_num in num_list :
    ans += int(hidden_num)

print(ans)