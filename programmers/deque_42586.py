from collections import deque
import math

def solution(progresses, speeds):
    answer = []

    progresses = deque(progresses)
    speeds = deque(speeds)

    tmp = 0

    while progresses :
        progress = progresses.popleft()
        speed = speeds.popleft()
        day = 0
        day += math.ceil((100 - progress) / speed)
        tmp += 1

        while progresses and speeds and progresses[0] + (speeds[0] * day) >= 100 :
            tmp += 1
            progresses.popleft()
            speeds.popleft()
        
        answer.append(tmp)
        tmp = 0


    return answer


print(solution([93, 30, 55], [1, 30, 5]))
