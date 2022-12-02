import sys
sys.stdin = open("C:/Users/mmm/Desktop/SWjungle/prac_python/input.txt","r")

insert_char = sys.stdin.readline()
# print(insert_char)

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i","j","k","l", "m", "n", "o", "p", "q", "r","s","t","u","v","w","x","y","z"]

cnt = 0
for check in alphabet :
    if check in insert_char :
        print(insert_char.index(check), end = " ")
    else :
        print('-1', end = " ")