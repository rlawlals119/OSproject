import sys
from PyQt5 import uic
import numpy as np
from PyQt5.QtWidgets import *
import heapq
import queue
import copy


form_class = uic.loadUiType("./UI.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self, parent=None):
        super(WindowClass, self).__init__(parent)
        self.PROCESSES = 0
        self.T_QUANTUM = 0
        self.PRIORITY = list(np.zeros(15))
        self.at = 0
        self.bt = 0
        self.AT = list(np.zeros(20))
        self.hrrn_AT = list(np.zeros(15))
        self.BT = list(np.zeros(15))
        self.TT = []
        self.WT = []
        self.name = 0
        self.max_time = 0
        self.setupUi(self)

        self.start_pushButton.clicked.connect(self.startBtn)
        self.Add_pushButton.clicked.connect(self.addBtn)
        self.Reset_pushButton.clicked.connect(self.resetBtn)

    def startBtn(self):
        self.PROCESSES = self.name
        self.max_time = sum(self.BT)
        current_Algorithm = str(self.AlgorithomList_comboBox.currentText())
        at_tmp = self.AT.copy()
        for i in range(1, self.at+1):
            if self.AT[i] != 0: self.hrrn_AT[at_tmp[i]] = i
        if current_Algorithm == "FCFS":
            self.WT, self.TT = self.fcfs_ui(self.PROCESSES, 0, self.AT, self.BT, self.at)
        elif current_Algorithm == "RR":
            self.T_QUANTUM = int(self.lineEdit_3.text())
            self.WT, self.TT = self.rr_ui(self.PROCESSES, 0, self.AT, self.BT, self.at, self.T_QUANTUM)
        elif current_Algorithm == "SPN":
            self.WT, self.TT = self.spn_ui(self.PROCESSES, 0, self.AT, self.BT, self.at)
        elif current_Algorithm == "SRTN":
            self.WT, self.TT = self.srtn_ui(self.PROCESSES, 0, self.AT, self.BT, self.at)
        elif current_Algorithm == "HRRN":
            self.WT, self.TT = self.hrrn_ui(self.PROCESSES, 0, self.hrrn_AT, self.BT)
        elif current_Algorithm == "TPFS":
            self.WT, self.TT = self.tpfs_ui(self.PROCESSES, 0, self.hrrn_AT, self.BT, self.PRIORITY)
        for i in range(0, self.PROCESSES):
            self.ResultTable_tableWidget.setItem(i, 0, QTableWidgetItem(str(i+1)))
            if current_Algorithm == "HRRN" or current_Algorithm == "TPFN":
                self.ResultTable_tableWidget.setItem(i, 1, QTableWidgetItem(str(self.hrrn_AT[i+1])))
            else : 
                self.ResultTable_tableWidget.setItem(i, 1, QTableWidgetItem(str(self.AT.index(i+1))))
            self.ResultTable_tableWidget.setItem(i, 2, QTableWidgetItem(str(self.BT[i+1])))
            self.ResultTable_tableWidget.setItem(i, 3, QTableWidgetItem(str(self.WT[i+1])))
            self.ResultTable_tableWidget.setItem(i, 4, QTableWidgetItem(str(self.TT[i+1])))
            self.ResultTable_tableWidget.setItem(i, 5, QTableWidgetItem(str(round(self.TT[i+1]/self.BT[i+1], 1))))

        self.show()
        

    def addBtn(self):
        self.name = int(self.ProcessName_textEdit.toPlainText())     # Process name 입력
        self.at = int(self.ArrivalTime_textEdit.toPlainText())       # Process 도착 시간
        self.AT[self.at] = self.name                                      # AT 인덱스 : 도착시간, 값 : 도착 process
        self.bt = int(self.BurstTime_textEdit.toPlainText())         # BT
        self.BT[self.name] = self.bt                                      # 인덱스 : process, 값 : bt
        self.PRIORITY[self.name] = int(self.Priority_textEdit.toPlainText())
        self.TimeTable_tableWidget.setItem(self.name-1, 0, QTableWidgetItem(str(self.name)))  # 테이블에 name표시
        self.TimeTable_tableWidget.setItem(self.name-1, 1, QTableWidgetItem(str(self.at)))    # 테이블에 AT표시
        self.TimeTable_tableWidget.setItem(self.name-1, 2, QTableWidgetItem(str(self.bt)))    # 테이블에 BT표시
        print(self.AT)
        print(self.BT)
        self.ProcessName_textEdit.clear()
        self.ArrivalTime_textEdit.clear()
        self.BurstTime_textEdit.clear()
        self.Priority_textEdit.clear()
        self.show()

    def resetBtn(self):
        self.TimeTable_tableWidget.clear()
        self.ResultTable_tableWidget.clear()

    def GanttChart(self, TIME, current_p):
        self.Ganttchart_tableWidget.setColumnCount(TIME)
        self.Ganttchart_tableWidget.setRowCount(1)
        self.Ganttchart_tableWidget.setItem(0, TIME, str(current_p))


    def fcfs_ui(self, PROCESSES, TIME, AT, BT, at):
        queue = []
        current_p = 0                   # 현재 프로세스
        tmp = BT.copy()
        TT = list(np.zeros(PROCESSES+1))
        WT = list(np.zeros(PROCESSES+1))
        while (TIME < self.max_time):
            if(TIME <= at and AT[TIME] != 0) : queue.append(tmp[AT[TIME]])
            TIME += 1
            if current_p == 0:          # 프로세서 할당 가능
                current_p = tmp.index(queue.pop(0)) # 현재 프로세서에 queue 원소 하나 넣음
                #self.GanttChart(TIME, current_p)
                print("proccess : ", current_p)        # 현재 프로세서 넘버 출력
            if current_p != 0:
                tmp[current_p] -= 1      # 현재 프로세스의 남은 수행 시간
                if tmp[current_p] == 0 : # 현재 프로세스 수행 완료 시
                    print("P{0}의 TT : {1}".format(current_p, TIME))    # 프로세스 실행 시간
                    TT[current_p] = TIME - AT.index(current_p)          # TT = 수행완료시간 - AT
                    WT[current_p] = TT[current_p] - BT[current_p]       # WT = TT - BT
                    current_p = 0       # 현재 프로세스 비워줌
        return WT, TT

    def rr_ui(self, PROCESSES, TIME, AT, BT, at,T_QUANTUM):
        queue = []
        TT = list(np.zeros(PROCESSES+1))
        WT = list(np.zeros(PROCESSES+1))
        current_p = 0                   # 현재 프로세스
        tmp = BT.copy()
        rr_t = T_QUANTUM
        if(AT[0] != 0) : queue.append(AT[TIME])
        while (TIME < self.max_time):
            TIME += 1
            if(TIME <= at and AT[TIME] != 0) : queue.append(AT[TIME])
            if current_p == 0 or rr_t == T_QUANTUM:          # 프로세서 할당 가능
                current_p = queue.pop(0) # 현재 프로세서에 queue 원소 하나 넣음
                print("proccess : ", current_p)        # 현재 프로세서 넘버 출력

            if current_p != 0:          # 프로세서 할당된 상태
                tmp[current_p] -= 1
                rr_t -= 1

                if tmp[current_p] == 0:  # 수행완료된 경우
                    print("P{0}의 TT : {1}".format(current_p, TIME))    # 프로세스 실행 시간
                    TT[current_p] = TIME - AT.index(current_p)          # TT = 수행완료시간 - AT
                    WT[current_p] = TT[current_p] - BT[current_p]       # WT = TT - BT
                    current_p = 0           # 현재 프로세스 비워줌
                    rr_t = T_QUANTUM

                elif rr_t == 0:         # 사용 제한 시간을 모두 수행한 경우
                    queue.append(current_p)
                    current_p = 0
                    rr_t = T_QUANTUM

        return WT, TT

    def spn_ui(self, PROCESSES, TIME, AT, BT, at):
        heap = []
        current_p = 0                   # 현재 프로세스
        tmp = BT.copy()
        TT = list(np.zeros(PROCESSES+1))
        WT = list(np.zeros(PROCESSES+1))
        print(AT)
        print(BT)
        while (TIME < self.max_time):
            if(TIME <= at and AT[TIME] != 0) : heapq.heappush(heap, tmp[AT[TIME]])
            TIME += 1
            if current_p == 0:          # 프로세서 할당 가능
                print(heap)
                current_p = tmp.index(heapq.heappop(heap)) # 현재 프로세서에 heap에서 가장 작은 원소 넣음
                print("proccess : ", current_p)        # 현재 프로세서 넘버 출력
            if current_p != 0:
                tmp[current_p] -= 1      # 현재 프로세스의 남은 수행 시간
                if tmp[current_p] == 0 : # 현재 프로세스 수행 완료 시
                    print("P{0}의 TT : {1}".format(current_p, TIME))    # 프로세스 실행 시간
                    TT[current_p] = TIME - AT.index(current_p)          # TT = 수행완료시간 - AT
                    WT[current_p] = TT[current_p] - BT[current_p]       # WT = TT - BT
                    current_p = 0       # 현재 프로세스 비워줌

        return WT, TT

    def srtn_ui(self, PROCESSES, TIME, AT, BT, at):
        heap = []
        current_p = 0   
        tmp = BT.copy()     
        TT = list(np.zeros(PROCESSES+1))
        WT = list(np.zeros(PROCESSES+1))           
        while (TIME < self.max_time):
            if(TIME <= at and AT[TIME] != 0) : heapq.heappush(heap, tmp[AT[TIME]])
            TIME += 1
            current_p = tmp.index(heapq.heappop(heap)) # 현재 프로세서에 heap에서 가장 작은 원소 넣음
            print("proccess : ", current_p)        # 현재 프로세서 넘버 출력
            if current_p != 0:
                tmp[current_p] -= 1      # 현재 프로세스의 남은 수행 시간
                heapq.heappush(heap, tmp[current_p])
                if tmp[current_p] == 0 : # 현재 프로세스 수행 완료 시
                    TT[current_p] = TIME - AT.index(current_p)          # TT = 수행완료시간 - AT
                    WT[current_p] = TT[current_p] - BT[current_p]       # WT = TT - BT
                    heapq.heappop(heap)
                    print("P{0}의 TT : {1}".format(current_p, TIME))    # 프로세스 실행 시간

        return WT, TT

    def hrrn_ui(self, PROCESSES, TIME, AT, BT):
        Done =  list(np.zeros(PROCESSES + 1))     # 완료 개수
        WT =    list(np.zeros(PROCESSES + 1))     # Waiting time
        TT =    list(np.zeros(PROCESSES + 1))     # Turnaround time
        NTT =   list(np.zeros(PROCESSES + 1))     # Normalized TT
        sum_BT = 0   # Burst Time 합계
        for i in range(1, PROCESSES + 1):       # 프로세스 개수만큼 생성
            #PROCESSES.append(chr(64 + i))      # 프로세스 이름 삽입 (A, B, C, D)
            sum_BT += BT[i]                     # BT 합계

        while(TIME < sum_BT):
            HRR = 0     # High Response Ratio
            NRR = 0     # Now Response Ratio
            index = 1   # Index 위치
            for i in range(1, PROCESSES + 1):
                if AT[i] <= TIME and Done[i] == 0:
                    NRR = (((TIME - AT[i]) + BT[i]) / BT[i])
                    if HRR < NRR:  # 가장 높은 Response Ratio 확인
                        HRR = NRR  # Response Ratio 저장 
                        index = i  # 프로세스 인덱스 위치
            TIME += BT[index]                   # 총 실행시간
            TT[index] = TIME - AT[index]        # Turn-Around Time 계산
            WT[index] = (TT[index] - BT[index]) # Waiting Time 계산
            NTT[index] = (TT[index] / BT[index])       # Normalized TT 계산
            Done[index] = 1       # 완료된 프로세스를 처리

        return WT, TT

    def tpfs_ui (self, PROCESSES, TIME, AT, BT, TIER):
        WT = list(np.zeros(PROCESSES + 1))
        TT = list(np.zeros(PROCESSES + 1))
        BANK = list(np.zeros(PROCESSES + 1))
        BT_R = copy.deepcopy(BT)
        completed = list(np.zeros(PROCESSES + 1))
        Flag = 0         # 가장 높은 Tier의 인덱스
        tmp = 0          # 가장 높은 Tier
        sum_BT = 0
        for i in range(1, PROCESSES + 1):
            sum_BT += BT[i]  # 모든 프로세스의 총 수행시간
        while TIME < sum_BT:
            tmp = 0
            for i in range(1, PROCESSES + 1):                  # 각각의 프로세스에 대해서
                if AT[i] <= TIME and completed[i] == 0:         # 도착 시간이 현재보다 빠르고, 스케줄링이 완료되지 않았다면.
                    BANK[i] = 1                            # BANK 1로 표시하여 리스트에 실행할 수 있음 나타낸다.
            for i in range(1, PROCESSES + 1):           # 각각의 프로세스에 대해서
                if BANK[i] == 1 and completed[i] == 0 and TIER[i] > tmp:  # 실행 가능하고 TIER가 가장 높으면 
                    Flag = i                        # 해당 인덱스를 저장하고
                    tmp = TIER[i]                   # TIER를 저장한다.
            BT_R[Flag] -= 1     # BT 1감소
            TIME += 1           # 시간 1 카운트
            for i in range(1, PROCESSES + 1):
                if BT_R[i] <= 0 and BANK[i] == 1:    # 완료된 프로세스를 처리
                    completed[i] = 1            # 1값을 주어 BANK가 1의 값을 가지지 못하도록 한다.
                    BANK[i] = 0                 # BANK의 값을 0으로 고정
                    TT[i] = TIME - AT[i]        # Turn-Around Time 계산
                    WT[i] = (TT[i] - BT[i])     # Waiting Time 계산

        return WT, TT


if __name__=="__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()