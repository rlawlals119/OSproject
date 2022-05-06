import sys
from PyQt5 import uic
import numpy as np
from PyQt5.QtWidgets import *
import heapq
import queue

import spn
import fcfs


form_class = uic.loadUiType("./UI.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self, parent=None):
        super(WindowClass, self).__init__(parent)
        self.PROCESSES = 0
        self.at = 0
        self.bt = 0
        self.AT = list(np.zeros(20))
        self.BT = list(np.zeros(15))
        self.TT = []
        self.WT = []
        self.name = 0
        self.setupUi(self)

        self.start_pushButton.clicked.connect(self.startBtn)
        self.Add_pushButton.clicked.connect(self.addBtn)

    def startBtn(self):
        self.PROCESSES = self.name
        self.WT, self.TT = self.spn_ui(self.PROCESSES, 0, self.AT, self.BT, self.at)
        for i in range(0, self.PROCESSES):
            self.ResultTable_tableWidget.setItem(i, 0, QTableWidgetItem(str(self.AT.index(i+1))))
            self.ResultTable_tableWidget.setItem(i, 1, QTableWidgetItem(str(self.BT[i+1])))
            self.ResultTable_tableWidget.setItem(i, 2, QTableWidgetItem(str(self.WT[i+1])))
            self.ResultTable_tableWidget.setItem(i, 3, QTableWidgetItem(str(self.TT[i+1])))

        self.show()
        

    def addBtn(self):
        self.name = int(self.ProcessName_textEdit.toPlainText())     # Process name 입력
        self.at = int(self.ArrivalTime_textEdit.toPlainText())       # Process 도착 시간
        self.AT[self.at] = self.name                                      # AT 인덱스 : 도착시간, 값 : 도착 process
        self.bt = int(self.BurstTime_textEdit.toPlainText())         # BT
        self.BT[self.name] = self.bt                                      # 인덱스 : process, 값 : bt
        self.TimeTable_tableWidget.setItem(self.name-1, 0, QTableWidgetItem(str(self.name)))  # 테이블에 name표시
        self.TimeTable_tableWidget.setItem(self.name-1, 1, QTableWidgetItem(str(self.at)))    # 테이블에 AT표시
        self.TimeTable_tableWidget.setItem(self.name-1, 2, QTableWidgetItem(str(self.bt)))    # 테이블에 BT표시
        print(self.AT)
        print(self.BT)
        self.show()

    def spn_ui(self, PROCESSES, TIME, AT, BT, at):
        heap = []
        current_p = 0                   # 현재 프로세스
        tmp = BT.copy()
        TT = list(np.zeros(PROCESSES+1))
        WT = list(np.zeros(PROCESSES+1))
        print(AT)
        print(BT)
        while (TIME < 20):
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

if __name__=="__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()