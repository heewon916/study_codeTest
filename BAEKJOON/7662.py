import sys
input = sys.stdin.readline
import heapq as hq
t = int(input())

for _ in range(t):
    k = int(input())

    min_h = []
    max_h = []
    isDel = [0] * k ##### POINT !!!!!!
    ## 삭제된 idx에 대해서 1로 표기하고, min_h와 max_h를 동기화하는 방법이다.
    # nums = {}
    for i in range(k):
        cmd, val = map(str, input().split())
        val = int(val)
        # del_i = -1
        if cmd == "I":
            hq.heappush(min_h, (val, i))
            hq.heappush(max_h, (-val, i))
            # nums[i] = val
            #print(cmd, val, min_h, max_h)
        else:
            if val == -1: # del min
                if min_h:
                    v, idx = hq.heappop(min_h)
                    isDel[idx] = 1
                    # del_i = idx
                    # nums.pop(idx)
                    # for j in range(len(max_h)):
                    #     if max_h[j][1] == idx:
                    #         max_h.pop(j)
                    #         break
                    # hq.heapify(max_h)
            elif val == 1: # del max
                if max_h:
                    v, idx = hq.heappop(max_h)
                    isDel[idx] = 1
                    # del_i = idx
                    # nums.pop(idx)
                    # for j in range(len(min_h)):
                    #     if min_h[j][1] == idx:
                    #         min_h.pop(j)
                    #         break
                    # hq.heapify(min_h)
        while max_h and isDel[max_h[0][1]]:
            # 맨 위에 있는 애가 삭제된 친구인지 확인하고 맞으면 삭제
            hq.heappop(max_h)
        while min_h and isDel[min_h[0][1]]:
            hq.heappop(min_h)

        # print('del_i', del_i)
        # if del_i != -1:
        # for j in range(len(min_h)):
        #     if min_h[j][1] == del_i:
        #         min_h.pop(j)
        # for j in range(len(max_h)):
        #     if max_h[j][1] == del_i:
        #         max_h.pop(j)
        # hq.heapify(min_h)
        # hq.heapify(max_h)
        # if del_i != -1:
        #     if min_h:
        #         min_h.pop(del_i)
        #         hq.heapify(min_h)
        #     if max_h:
        #         max_h.pop(del_i)
        #         hq.heapify(max_h)
        # print(cmd, val, min_h, max_h)

    if min_h and max_h:
        print(-max_h[0][0], min_h[0][0])
    else:
        print('EMPTY')
