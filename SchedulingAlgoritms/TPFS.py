'''
Tier Process First Service
중요도(1~3)를 설정한 선점 스케줄링
같은 중요도를 가진 프로세스는 먼저 선점한 프로세스가 끝까지 사용한다.
'''
import copy
import numpy as np
#from time import time, sleep

if __name__ == '__main__':

    E = 0
    P = 0
    PROCESSES = int(input("프로세스 수를 입력하시오. : "))  # 사용되는 프로세스 수 입력
    PROCESSOR = E + P
    W = 0

    TIER = [0] * PROCESSES   # 각 프로세스의 우선순위
    completed = [0] * PROCESSES  # 완료 개수
    WT = [0] * PROCESSES  # Waiting time
    TT = [0] * PROCESSES  # Turnaround time
    NTT = [0] * PROCESSES  # Normalized TT
    BANK = [0] * PROCESSES # 
    TIME = 0                # 프로그램 전체 수행 시간
    max_time = 0            # 프로세스의 총 수행시간(BT의 합계)

    ID = []                 # 프로세스
    for i in range(0, PROCESSES):    # 프로세스 개수만큼 생성
        ID.append(chr(65 + i))      # 프로세스 이름 삽입 (A, B, C, D)

    avg_WT = 0  # Waiting Time 평균
    avg_TT = 0  # Turn-around Time 평균

    #BT = list(np.zeros(PROCESSES))  # (0위치 비움)0으로 채워진 프로세스 수만큼의 크기를 가진 리스트
    BT = [1] * PROCESSES

    for i in range(0, PROCESSES):
        bt = int(input("P{0}의 BT : ".format(i)))  # bt 입력
        BT[i] = bt  # 인덱스를 프로세스 번호라고 생각하고 각 프로세스의 bt값 넣음
        max_time += bt  # 모든 프로세스의 총 수행시간

    BT_R = copy.deepcopy(BT)   # 뺄셈 연산을 진행할 BT의 값 깊은 복사

    #AT = list(np.zeros(PROCESSES))  # 0으로 채워진 총 수행시간 크기의 리스트
    AT = [0] * PROCESSES

    for i in range(0, PROCESSES):
        at = int(input("P{0}의 AT : ".format(i)))  # at 입력
        AT[i] = at  # 인덱스는 도착한 시간 넣어진 값은 프로세스의 번호

    TIER = list(np.zeros(PROCESSES))

    for i in range(0, PROCESSES):
        tier = int(input("P{0}의 TIER : ".format(i)))    # tier 입력
        if tier <= 1: TIER[i] = 1                        # 중요도를 1~3까지 설정
        elif tier == 2: TIER[i] = 2
        else: TIER[i] = 3

    # AT, BT, 총 BT, 현재 진행시간, TIER 출력
    print("PROCESSE", "\t", "AT", "\t\t",
          "BT", "\t\t", "WT", "\t\t",
          "TT", "\t\t", "NTT", "\t\t", "TIER")

    ##########################################################################
    ############################## 스케줄링 시작 ##############################
    ##########################################################################
    
    TIME = AT[0]     # 첫 프로세스 도착 시간 and 수행시간(초)
    Flag = 0         # 가장 높은 Tier의 인덱스
    tmp = 0          # 가장 높은 Tier

                ########################################################
                ###### TIER 우선순위에 따른 BT_R[i]을 1씩 차감 방법 ######
                ########################################################
    '''
    print("스케줄링 진행 전")
    for i in range(0, PROCESSES):
            print(AT[i], BT_R[i], WT[i], TT[i], TIME)
    '''

    # BT 합계까지 TIME을 증가시킨다.
    while TIME < max_time:
        tmp = 0

        for i in range(0, PROCESSES):                  # 각각의 프로세스에 대해서
            if AT[i] <= TIME and completed[i] == 0:         # 도착 시간이 현재보다 빠르고, 스케줄링이 완료되지 않았다면.
                BANK[i] = 1                            # BANK 1로 표시하여 리스트에 실행할 수 있음 나타낸다.
                ####print("i번째는 ", i)                    ######## 진행 확인 ########

        for i in range(0, PROCESSES):           # 각각의 프로세스에 대해서
            if BANK[i] == 1 and completed[i] == 0 and TIER[i] > tmp:  # 실행 가능하고 TIER가 가장 높으면 
                Flag = i                        # 해당 인덱스를 저장하고
                tmp = TIER[i]                   # TIER를 저장한다.

        BT_R[Flag] -= 1     # BT 1감소
        TIME += 1           # 시간 1 카운트
        
                ########################################################
                ################## 스케줄링 진행에 따른 ##################
                ################## TIME과 최고 TIER 확인 ################
            
        '''
        print("TIME은 ", TIME)
        print("TIER는 ", tmp)
        print()
        '''
            # 도착한 프로세스에 대해서 BANK == 1로 구분지어 TIER를 비교한다.
            # Flag 변수로 TIER가 가장 큰 인덱스 저장하기
            # TIME을 1씩 더하며 해당 인덱스의 BT_R을 1 차감한다.    
            # BT_R이 0이 되면 BANK에서 뺀다.
            
                ########################################################
                #####우선순위에 따른 정렬 이후 BT_R[i]을 1씩 차감 방법#####
                ########################################################
        
                ########################################################
                ##################  스케줄링 진행상황   ##################
        '''
        print("스케줄링 진행중")
        for i in range(0, PROCESSES):
            print(AT[i], BT_R[i], WT[i], TT[i], TIME)
        '''

        for i in range(0, PROCESSES):
            if BT_R[i] <= 0 and BANK[i] == 1:    # 완료된 프로세스를 처리
                completed[i] = 1     # 1값을 주어 BANK가 1의 값을 가지지 못하도록 한다.
                BANK[i] = 0     # BANK의 값을 0으로 고정
                TT[i] = TIME - AT[i]        # Turn-Around Time 계산
                #print(TT[i])
                WT[i] = (TT[i] - BT[i])     # Waiting Time 계산
                #print(WT[i])
                NTT = (TT[i] / BT[i])       # Normalized TT 계산
                #print(NTT)

                avg_TT += TT[i]   # Turn-Around Time 평균 계산을 위한 합계 구하는 중
                avg_WT += WT[i]   # Waiting Time 평균 계산을 위한 합계 구하는 중

                # 스케줄링이 끝나는 순서대로 출력
                print(ID[i], "\t\t", AT[i], "\t\t",
                    BT[i], "\t\t", WT[i], "\t\t",
                    TT[i], "\t\t", "{0:.2f}".format(NTT),
                    "\t\t", tmp)

    print("WT 평균: {0:.2f}".format(avg_WT / PROCESSES))
    print("TT 평균: {0:.2f}".format(avg_TT / PROCESSES))