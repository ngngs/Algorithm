import heapq
from collections import deque

def solution(jobs):

    tmp = []
    spend_time = 0
    now = 0
    jobs.sort()
    jobs_num = len(jobs)

    jobs = deque(jobs)
    first = jobs.popleft()
    heapq.heappush(tmp, [first[1], first[0]])

    while tmp :
        spent, start = heapq.heappop(tmp)

        if now > start :
            spend_time += now-start+spent
            now += spent 
        else :
            spend_time += spent
            now = start + spent
    
        while jobs :
            _start, _spent = jobs.popleft()
            if _start <= now :
                heapq.heappush(tmp, [_spent, _start])
            else :
                if not tmp :
                    heapq.heappush(tmp, [_spent, _start])
                    break
                jobs.appendleft([_start,_spent])
                break


    return spend_time // jobs_num

print(solution([[0, 3], [1, 9], [500, 6]]))
