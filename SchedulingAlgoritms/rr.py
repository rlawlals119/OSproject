from calendar import c
import queue
import numpy as np
from time import time, sleep
from queue import Queue

PROCCESSES = int(input("프로세스 수를 입력하시오. : ")) # 사용되는 프로세스 수 입력
PROCCESSORS = 1
TIME = 0        # 프로그램 전체 수행 시간
T_QUANTUM = 3
max_time = 20    # 모든 BT를 합한 값, 모든 프로세스의 총 수행 시간
bt = 0
at = 0      # 입력받은 BT, AT 값

AT = [1, 2, 0, 3, 0, 4, 5]
BT = [0, 3, 7, 2, 5, 3]
TT = list(np.zeros(PROCCESSES+1))
WT = list(np.zeros(PROCCESSES+1))
# TT = 수행완료시간 - AT
# WT = TT - BT
#BT = list(np.zeros(PROCCESSES+1))                   # (0위치 비움)0으로 채워진 프로세스 수만큼의 크기를 가진 리스트
#
#for i in range(0, PROCCESSES):
#    bt = int(input("P{0}의 BT : ".format(i+1)))     # bt 입력
#    BT[i+1] = bt                                    # 인덱스를 프로세스 번호라고 생각하고 각 프로세스의 bt값 넣음
#    max_time += bt                                  # 모든 프로세스의 총 수행시간

tmp = BT.copy()

#AT = list(np.zeros(max_time))                       # 0으로 채워진 총 수행시간 크기의 리스트
#
#for i in range(0, PROCCESSES):
#    at = int(input("P{0}의 AT : ".format(i+1)))     # at 입력
#    AT[at] = i+1                                    # 인덱스는 도착한 시간 넣어진 값은 프로세스의 번호

print(AT)
print(BT)
print(tmp)

queue = []
current_p = 0                   # 현재 프로세스
start = time()                  # 시작 시간
rr_t = T_QUANTUM
if(AT[0] != 0) : queue.append(AT[TIME])
while (TIME < max_time):
    TIME += 1
    if(TIME <= 6 and AT[TIME] != 0) : queue.append(AT[TIME])
    if current_p == 0 or rr_t == T_QUANTUM:          # 프로세서 할당 가능
        current_p = queue.pop(0) # 현재 프로세서에 queue 원소 하나 넣음
        print("proccess : ", current_p)        # 현재 프로세서 넘버 출력

    if current_p != 0:          # 프로세서 할당된 상태
        tmp[current_p] -= 1
        rr_t -= 1

        if tmp[current_p] == 0:  # 수행완료된 경우
            print("P{0}의 TT : {1}".format(current_p, TIME))    # 프로세스 실행 시간
            TT[current_p] = TIME - AT.index(current_p)
            WT[current_p] = TT[current_p] - BT[current_p]
            current_p = 0           # 현재 프로세스 비워줌
            rr_t = T_QUANTUM

        elif rr_t == 0:         # 사용 제한 시간을 모두 수행한 경우
            queue.append(current_p)
            current_p = 0
            rr_t = T_QUANTUM

print("P id| AT | BT | WT | TT")
for i in range (1, PROCCESSES+1):
    print("P{0} | {1} | {2} | {3} | {4}".format(i, AT.index(i), BT[i], WT[i], TT[i]))
end = time()

print(end - start)