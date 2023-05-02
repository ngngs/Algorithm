from heapq import *

def solution(operations):

    heap = []    
    for operation in operations :
        command, value = operation.split(" ")[0], int(operation.split(" ")[1])
        if command == "I" :
            heappush(heap, value)
        else :
            if heap :
                if value == -1 :
                    heappop(heap)
                else :
                    heap = nlargest(len(heap), heap)[1:]
                    heapify(heap)

    if heap :
        _min, _max = heappop(heap), nlargest(1, heap)[0]
        ans = [_max, _min]
    else :
        ans = [0, 0]

    return ans

