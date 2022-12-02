import sys
sys.stdin = open("C:/Users/mmm/Desktop/SWjungle/prac_python/input.txt","r")

insert_char = list(sys.stdin.readline())
# print(insert_char)

char_dict = {}

for char in insert_char :
    if char not in char_dict :
        char_dict[char] = 1
    else :
        char_dict[char] += 1

print(char_dict.values())
ans_dict = {}
value = char_dict.values()
for val in value :
    if val not in ans_dict :
        ans_dict[val] = 1
    else :
        ans_dict[val] += 1

print(ans_dict.values())
