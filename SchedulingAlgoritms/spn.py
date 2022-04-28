import heapq
import numpy as np
from time import time, sleep

PROCCESSES = int(input("프로세스 수를 입력하시오. : ")) # 사용되는 프로세스 수 입력
PROCCESSORS = 1
TIME = 0        # 프로그램 전체 수행 시간
max_time = 0    # 모든 BT를 합한 값, 모든 프로세스의 총 수행 시간
bt = 0
at = 0      # 입력받은 BT, AT 값

BT = list(np.zeros(PROCCESSES+1))                   # (0위치 비움)0으로 채워진 프로세스 수만큼의 크기를 가진 리스트
AT = list(np.zeros(PROCCESSES+1))

AT[0] = -1
for i in range(0, PROCCESSES):
    at = int(input("P{0}의 AT : ".format(i+1)))     # at 입력
    bt = int(input("P{0}의 BT : ".format(i+1)))     # bt 입력
    AT[i+1] = at
    BT[i+1] = bt                                    # 인덱스를 프로세스 번호라고 생각하고 각 프로세스의 bt값 넣음
    max_time += bt                                  # 모든 프로세스의 총 수행시간

#AT = list(np.zeros(max_time))                       # 0으로 채워진 총 수행시간 크기의 리스트
#
#for i in range(0, PROCCESSES):
#    at = int(input("P{0}의 AT : ".format(i+1)))     # at 입력
#    AT[at] = i+1                                    # 인덱스는 도착한 시간 넣어진 값은 프로세스의 번호

print(AT)
print(BT)

heap = []
current_p = 0                   # 현재 시간
start = time()                  # 시작 시간
while (TIME < max_time):
    if(TIME <= at and AT.index(TIME) != -1) : heapq.heappush(heap, BT[AT.index(TIME)])
    TIME += 1
    if current_p == 0:          # 프로세서 할당 가능
        current_p = BT.index(heapq.heappop(heap)) # 현재 프로세서에 heap에서 가장 작은 원소 넣음
        print("proccess : ", current_p)        # 현재 프로세서 넘버 출력
    if current_p != 0:
        BT[current_p] -= 1      # 현재 프로세스의 남은 수행 시간
        if BT[current_p] == 0 : # 현재 프로세스 수행 완료 시
            current_p = 0       # 현재 프로세스 비워줌
            print("P{0}의 TT : {1}".format(current_p, TIME))    # 프로세스 실행 시간

end = time()

print(end - start)