import sys
sys.stdin = open("C:/Users/mmm/Desktop/SWjungle/prac_python/input.txt","r")

while True :
    sentence = sys.stdin.readline().rstrip()
    if sentence == '.' :
        break
        
    # print(sentence)
    bracket_append_list = ['(', '[']
    bracket_pop_list = [')', ']']
    check_list = []
    ans = True
    for i in range(len(sentence)) :
        # print(check_list)
        if check_list == [] :
            if sentence[i] in bracket_pop_list :
                ans = False
                break

        if sentence[i] in bracket_append_list :
            check_list.append(sentence[i])
        elif sentence[i] in bracket_pop_list :
            if (sentence[i] == ')' and check_list[-1] == '[') :
                ans = False
                break
            elif (sentence[i] == ']' and check_list[-1] == '(') :
                ans = False
                break
            else :
                check_list.pop()
        else :
            pass

    if check_list == [] and ans == True :
        print('yes')
    else :
        print('no')
    # print(sentence_list)
    