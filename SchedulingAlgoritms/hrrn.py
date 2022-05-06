'''
# 코드 시작
if __name__ == '__main__':
    PROCESSE = 5 # 프로세스 개수 설정
    W = 0        # 소비전력
     
    Done =  [0] * (PROCESSE+1)     # 완료 개수
    WT =    [0] * (PROCESSE+1)     # Waiting time
    TT =    [0] * (PROCESSE+1)     # Turnaround time
    NTT =   [0] * (PROCESSE+1)     # Normalized TT
    
    AT = [0, 0, 1, 3, 5, 6]    # Arrival Times 설정   
    BT = [0, 3, 7, 2, 5, 3]    # Burst Times 설정
    PROCESSES = [0]          # 프로세스

    sum_BT = 0   # Burst Time 합계
    avg_WT = 0   # Waiting Time 평균
    avg_TT = 0   # Turn-around Time 평균
     
    # 프로세스 이름 지정 (A, B, C, D)
    for i in range(1, PROCESSE + 1):    # 프로세스 개수만큼 생성
        PROCESSES.append(chr(64 + i))      # 프로세스 이름 삽입 (A, B, C, D)
        sum_BT += BT[i]             # BT 합계
         
    # Arriaval Time 대로 정렬한다.
    for i in range(1, PROCESSE):        # i: 0부터 3까지
        for j in range(i + 2, PROCESSE + 1):    # j: 1부터 4까지 ex) (0,1), (0,2)
            if AT[i] > AT[j]:               # AT의 대소비교
                AT[i], AT[j] = AT[j], AT[i] # AT가 빠른 프로세스와 바꾼다.
    
    
    #for i in range(0, 5):
    #    print(ID[i] )
    

    print("#### WT = TT - BT ####", "\t\t", "#### NTT = TT/BT ####")
    print("PROCESS", "\t", "AT", "\t\t",
          "BT", "\t\t", "WT", "\t\t",
          "TT", "\t\t", "NTT")

    ##########################################################################
    ############################## 스케줄링 시작 ##############################
    ##########################################################################

    TIME = AT[1]     # 첫 프로세스 도착 시간 and 수행시간(초)

    # BT 합계까지 TIME을 증가시킨다.
    while(TIME < sum_BT):
        # 응답률 설정 (Response Ratio = (WT + BT) / BT))
        HRR = 0     # High Response Ratio
        NRR = 0     # Now Response Ratio
        index = 0   # Index 위치
        
        for i in range(1, PROCESSE+1):
            
            # 프로세스가 도착했을 때를 확인한다.
            # 도착 시간이 현재보다 빠르고, 스케줄링이 완료되지 않았다면.
            # 완료를 판별 0: 처리 이전, 1: 처리 완료
            if AT[i] <= TIME and Done[i] == 0:
                 
                # Now Response Ratio 계산 (Response Ratio = (WT + BT) / BT))
                NRR = (((TIME - AT[i]) + BT[i]) / BT[i])
                          
                if HRR < NRR:  # 가장 높은 Response Ratio 확인
                    HRR = NRR  # Response Ratio 저장 
                    index = i  # 프로세스 인덱스 위치
                    
        # Highest Response Ratio을 가진 프로세스를 처리
        TIME += BT[index]                   # 총 실행시간
        TT[index] = TIME - AT[index]        # Turn-Around Time 계산
        WT[index] = (TT[index] - BT[index]) # Waiting Time 계산
        NTT = (TT[index] / BT[index])       # Normalized TT 계산

        avg_TT += TT[index]   # Turn-Around Time 평균 계산
        avg_WT += WT[index]   # Waiting Time 평균 계산
        
        Done[index] = 1       # 완료된 프로세스를 처리
        
        # 스케줄링이 끝나는 순서대로 출력
        print(PROCESSES[index], "\t\t", AT[index], "\t\t",
              BT[index], "\t\t", WT[index], "\t\t",
              TT[index], "\t\t",
              "{0:.2f}".format(NTT))
        
    print("WT 평균: {0:.2f}".format(avg_WT / PROCESSE))
    print("TT 평균: {0:.2f}".format(avg_TT / PROCESSE))
    print(TIME) 
'''
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
import heapq
import numpy as np
import copy

def hrrn (PROCESSES, TIME, AT, BT, at):
    Done =  list(np.zeros(PROCESSES + 1))     # 완료 개수
    WT =    list(np.zeros(PROCESSES + 1))     # Waiting time
    TT =    list(np.zeros(PROCESSES + 1))     # Turnaround time
    NTT =   list(np.zeros(PROCESSES + 1))     # Normalized TT
    PROCESSES = [0]                         # 프로세스
    sum_BT = 0   # Burst Time 합계
    for i in range(1, PROCESSES + 1):       # 프로세스 개수만큼 생성
        #PROCESSES.append(chr(64 + i))      # 프로세스 이름 삽입 (A, B, C, D)
        sum_BT += BT[i]                     # BT 합계
    for i in range(1, PROCESSES + 1):           # AT 정렬
        for j in range(i + 2, PROCESSES + 1):    # j: 1부터 5까지 ex) (0,1), (0,2)
            if AT[i] > AT[j]:               # AT의 대소비교
                AT[i], AT[j] = AT[j], AT[i] # AT가 빠른 프로세스와 바꾼다.
    while(TIME < sum_BT):
        HRR = 0     # High Response Ratio
        NRR = 0     # Now Response Ratio
        index = 0   # Index 위치
        for i in range(1, PROCESSES + 1):
            if AT[i] <= TIME and Done[i] == 0:
                NRR = (((TIME - AT[i]) + BT[i]) / BT[i])
                if HRR < NRR:  # 가장 높은 Response Ratio 확인
                    HRR = NRR  # Response Ratio 저장 
                    index = i  # 프로세스 인덱스 위치
        TIME += BT[index]                   # 총 실행시간
        TT[index] = TIME - AT[index]        # Turn-Around Time 계산
        WT[index] = (TT[index] - BT[index]) # Waiting Time 계산
        NTT = (TT[index] / BT[index])       # Normalized TT 계산
        Done[index] = 1       # 완료된 프로세스를 처리
    print("P id| AT | BT | WT | TT")
    for i in range (1, PROCESSES+1):
        print("P{0} | {1} | {2} | {3} | {4}".format(i, AT[i], BT[i], WT[i], TT[i]))

    return WT, TT