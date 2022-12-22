# import sys
# from collections import deque
# sys.stdin = open("C:/Users/mmm/Desktop/SWjungle/prac_python/input.txt","r")

# def move_delete_function(val1, before_sentence) :
#     if val1 == 'L' :
#         cursor_point = before_sentence.index(".")

#         if cursor_point == 0 :
#             pass
#         else :
#             before_sentence[cursor_point - 1], before_sentence[cursor_point] = before_sentence[cursor_point], before_sentence[cursor_point - 1]
    
#     elif val1 == 'R' :
#         cursor_point = before_sentence.index(".")

#         if cursor_point == len(before_sentence) - 1 :
#             pass
#         else :
#             before_sentence[cursor_point], before_sentence[cursor_point + 1] = before_sentence[cursor_point + 1], before_sentence[cursor_point]

#     else :  # 'B' 삭제
#         cursor_point = before_sentence.index(".")
#         if cursor_point == 0 :
#             pass
#         else :
#             del before_sentence[cursor_point - 1]

# def insert_function(val1, val2, before_sentence) :
#     cursor_point = before_sentence.index(".")
#     before_sentence.insert(cursor_point, val2)

# before_sentence = list(sys.stdin.readline().rstrip() + '.')   # .은 커서의 위치

# m = int(input())
# # print(m)

# insert_list = deque()
# for _ in range(m) :
#     insert_list.append(sys.stdin.readline().rstrip().split())

# while len(insert_list) != 0 :
#     check_command = insert_list.popleft()
#     command = check_command[0]
#     if command == 'P'  :
#         insert_val = check_command[1]
#         insert_function(command, insert_val, before_sentence)
#     else :
#         move_delete_function(command, before_sentence)

# before_sentence.remove('.')
# for i in before_sentence :
#     print(i, end="")




# import sys
# from collections import deque
# sys.stdin = open("C:/Users/mmm/Desktop/SWjungle/prac_python/input.txt","r")

# def move_delete_function(val1, sentence, cursor_pos) :
#     if val1 == 'L' :
#         if cursor_pos == 0 :
#             pass
#         else :
#             cursor_pos -= 1
    
#     elif val1 == 'D' :
#         if cursor_pos == len(sentence) :
#             pass
#         else :
#             cursor_pos += 1

#     else :  # 'B' 삭제
#         if cursor_pos == 0 :
#             pass
#         else :
#             sentence = sentence[:cursor_pos - 1] + sentence[cursor_pos:]
#             cursor_pos -= 1
#     return sentence, cursor_pos

# def insert_function(val1, val2, sentence, cursor_pos) :
#     sentence = sentence[:cursor_pos] + val2 + sentence[cursor_pos:]
#     cursor_pos += 1
#     return sentence, cursor_pos

# sentence = sys.stdin.readline().rstrip()   # .은 커서의 위치
# cursor_pos = len(sentence)
# m = int(input())
# # print(m)

# operation_stack = deque()
# for _ in range(m) :
#     operation_stack.append(sys.stdin.readline().rstrip().split())

# while operation_stack :
#     command, *args = operation_stack.popleft()
#     if command == 'P'  :
#         insert_val = args[0]
#         sentence, cursor_pos = insert_function(command, insert_val, sentence, cursor_pos)
#     else :
#         sentence, cursor_pos = move_delete_function(command, sentence, cursor_pos)
# print(sentence)


import sys
from collections import deque
sys.stdin = open("C:/Users/mmm/Desktop/SWjungle/prac_python/input.txt","r")

def cursor_function(command, deque_left, deque_right) :
    if command == 'L' :
        if deque_left :
            deque_right.appendleft(deque_left.pop())
        else : 
            pass
    elif command == 'D' :
        if deque_right :
            deque_left.append(deque_right.popleft())
        else :
            pass
    else :
        if deque_left :
            deque_left.pop()
        else :
            pass

    return deque_left, deque_right

def insert_function(args, deque_left) :
    deque_left.append(args)
    return deque_left

sentence = sys.stdin.readline().strip()
# print(sentence)

n = len(sentence)
m = int(input())
# print(n, m)

deque_left = deque(sentence)
deque_right = deque()
# print(deque_left)

operation_stack = deque()
for _ in range(m) :
    operation_stack.append(sys.stdin.readline().strip().split())

while operation_stack :
    command, *args = operation_stack.popleft()
    if command == 'P' :
        args = args[0]
        deque_left = insert_function(args, deque_left)
    else :
        deque_left, deque_right = cursor_function(command, deque_left, deque_right)

ans = deque_left
for _ in range(len(deque_right)) :
    ans.append(deque_right.popleft())

print(''.join(ans))
