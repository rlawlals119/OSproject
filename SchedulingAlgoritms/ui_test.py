import sys
from PyQt5 import uic
import numpy as np
from PyQt5.QtWidgets import *
import heapq

import spn


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

        self.setupUi(self)

        self.start_pushButton.clicked.connect(self.startBtn)
        self.Add_pushButton.clicked.connect(self.addBtn)

    def startBtn(self):
        self.PROCESSES = self.BT.index(self.bt)
        self.WT, self.TT = spn.spn(self.PROCESSES, 0, self.AT, self.BT, self.at)
        for i in range(0, self.PROCESSES):
            self.ResultTable_tableWidget.setItem(i, 0, QTableWidgetItem(str(self.AT.index(i+1))))
            self.ResultTable_tableWidget.setItem(i, 1, QTableWidgetItem(str(self.BT[i+1])))
            self.ResultTable_tableWidget.setItem(i, 2, QTableWidgetItem(str(self.WT[i+1])))
            self.ResultTable_tableWidget.setItem(i, 3, QTableWidgetItem(str(self.TT[i+1])))

        self.show()
        

    def addBtn(self):
        name = int(self.ProcessName_textEdit.toPlainText())     # Process name 입력
        self.at = int(self.ArrivalTime_textEdit.toPlainText())       # Process 도착 시간
        self.AT[self.at] = name                                      # AT 인덱스 : 도착시간, 값 : 도착 process
        self.bt = int(self.BurstTime_textEdit.toPlainText())         # BT
        self.BT[name] = self.bt                                      # 인덱스 : process, 값 : bt
        self.TimeTable_tableWidget.setItem(name-1, 0, QTableWidgetItem(str(name)))  # 테이블에 name표시
        self.TimeTable_tableWidget.setItem(name-1, 1, QTableWidgetItem(str(self.at)))    # 테이블에 AT표시
        self.TimeTable_tableWidget.setItem(name-1, 2, QTableWidgetItem(str(self.bt)))    # 테이블에 BT표시
        self.show()

if __name__=="__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()