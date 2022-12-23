import sys
sys.stdin = open("C:/Users/mmm/Desktop/SWjungle/prac_python/input.txt","r")

import sys

n, k = map(int, input().split())
if k < 5 :
    print(0)
    exit()
    
elif k == 26 :
    print(n)
    exit()

ans = 0
words = [set(sys.stdin.readline().rstrip()) for _ in range(n)]
graph = [0] * 26

for alpha in ('a', 'c', 'i', 'n', 't') :
    graph[ord(alpha) - ord('a')] = 1

def dfs(idx, cnt) :
    global ans

    if cnt == k - 5 :
        readcnt = 0
        for word in words :
            check = True
            for w in word :
                if not graph[ord(w) - ord('a')] :   # 이미 배운 단어
                    check = False
                    break
            if check :                              # 배운 적이 없는 단어
                readcnt += 1
        ans = max(ans, readcnt)
        return

    for i in range(idx, 26) :
        if not graph[i] :
            graph[i] = True
            dfs(i, cnt + 1)
            graph[i] = False

dfs(0, 0)
print(ans)



# res = 0
# for _ in range(n) :
#     _a, _n, _t, _a, *args, _t, _i, _c, _a = list(sys.stdin.readline().rstrip())
#     # print(args)

#     word_dict = {'a' : 3, 'n' : 1, 't' : 2, 'c' : 1, 'i' : 1} 
#     for word in args :
#         if word not in word_dict.keys() :
#             word_dict[word] = 1
#         else :
#             word_dict[word] += 1
#         # print(word_dict)

#     print(word_dict)
#     # if len(list(word_dict.keys())) <= k :
#         # res += 1

# # print(res)


    
