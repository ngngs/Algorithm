def solution(n):
    answer = 0
    dp = [0 for _ in range(101)]
    # print(dp)
    dp[0] = 0
    dp[1] = 1
    dp[2] = 2
    
    for i in range(3, 101) :
        tmp = dp[i-1] + 1
        cnt = 0
        
        while "3" in str(tmp) or tmp % 3 == 0 :
            tmp += 1
            cnt += 1
        


        dp[i] = dp[i-1] + 1 + cnt
    print(dp)
    return answer

solution(7)