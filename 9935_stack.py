import sys
sys.stdin = open("C:/Users/mmm/Desktop/SWjungle/prac_python/input.txt","r")

sentence = sys.stdin.readline().strip()
bomb_word = sys.stdin.readline().strip()
check_num = len(bomb_word)

check = []
for i in range(len(sentence)) :
    check.append(sentence[i])
    if bomb_word == ("".join(check[-check_num:])) :
        for _ in range(check_num) :
            check.pop()

if check :
    print("".join(check))
else :
    print('FRULA')