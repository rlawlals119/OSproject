# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'OS_Project_GUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(932, 945)
        self.AlgorithomList_label = QtWidgets.QLabel(Dialog)
        self.AlgorithomList_label.setGeometry(QtCore.QRect(30, 20, 101, 16))
        self.AlgorithomList_label.setObjectName("AlgorithomList_label")
        self.ProcessName_label = QtWidgets.QLabel(Dialog)
        self.ProcessName_label.setGeometry(QtCore.QRect(150, 20, 101, 16))
        self.ProcessName_label.setObjectName("ProcessName_label")
        self.ProcessName_textEdit = QtWidgets.QTextEdit(Dialog)
        self.ProcessName_textEdit.setGeometry(QtCore.QRect(150, 50, 104, 31))
        self.ProcessName_textEdit.setObjectName("ProcessName_textEdit")
        self.ArrivalTime_label = QtWidgets.QLabel(Dialog)
        self.ArrivalTime_label.setGeometry(QtCore.QRect(270, 20, 101, 16))
        self.ArrivalTime_label.setObjectName("ArrivalTime_label")
        self.ArrivalTime_textEdit = QtWidgets.QTextEdit(Dialog)
        self.ArrivalTime_textEdit.setGeometry(QtCore.QRect(270, 50, 104, 31))
        self.ArrivalTime_textEdit.setObjectName("ArrivalTime_textEdit")
        self.BurstTime_label = QtWidgets.QLabel(Dialog)
        self.BurstTime_label.setGeometry(QtCore.QRect(390, 20, 101, 16))
        self.BurstTime_label.setObjectName("BurstTime_label")
        self.BurstTime_textEdit = QtWidgets.QTextEdit(Dialog)
        self.BurstTime_textEdit.setGeometry(QtCore.QRect(390, 50, 104, 31))
        self.BurstTime_textEdit.setObjectName("BurstTime_textEdit")
        self.Priority_label = QtWidgets.QLabel(Dialog)
        self.Priority_label.setGeometry(QtCore.QRect(510, 20, 101, 16))
        self.Priority_label.setObjectName("Priority_label")
        self.Priority_textEdit = QtWidgets.QTextEdit(Dialog)
        self.Priority_textEdit.setGeometry(QtCore.QRect(510, 50, 104, 31))
        self.Priority_textEdit.setObjectName("Priority_textEdit")
        self.Add_pushButton = QtWidgets.QPushButton(Dialog)
        self.Add_pushButton.setGeometry(QtCore.QRect(660, 50, 93, 28))
        self.Add_pushButton.setObjectName("Add_pushButton")
        self.Reset_pushButton = QtWidgets.QPushButton(Dialog)
        self.Reset_pushButton.setGeometry(QtCore.QRect(790, 50, 93, 28))
        self.Reset_pushButton.setObjectName("Reset_pushButton")
        self.ProcessNumber_label = QtWidgets.QLabel(Dialog)
        self.ProcessNumber_label.setGeometry(QtCore.QRect(640, 130, 121, 16))
        self.ProcessNumber_label.setObjectName("ProcessNumber_label")
        self.ExecutionSpeed_label = QtWidgets.QLabel(Dialog)
        self.ExecutionSpeed_label.setGeometry(QtCore.QRect(640, 170, 121, 16))
        self.ExecutionSpeed_label.setObjectName("ExecutionSpeed_label")
        self.ProcessorNumber_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.ProcessorNumber_lineEdit.setGeometry(QtCore.QRect(780, 130, 91, 21))
        self.ProcessorNumber_lineEdit.setObjectName("ProcessorNumber_lineEdit")
        self.ExecutionSpeed_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.ExecutionSpeed_lineEdit.setGeometry(QtCore.QRect(780, 170, 91, 21))
        self.ExecutionSpeed_lineEdit.setObjectName("ExecutionSpeed_lineEdit")
        self.RRTimeQuantum_label = QtWidgets.QLabel(Dialog)
        self.RRTimeQuantum_label.setGeometry(QtCore.QRect(640, 210, 121, 16))
        self.RRTimeQuantum_label.setObjectName("RRTimeQuantum_label")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(780, 210, 51, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(840, 210, 71, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(880, 170, 31, 16))
        self.label_10.setObjectName("label_10")
        self.start_pushButton = QtWidgets.QPushButton(Dialog)
        self.start_pushButton.setGeometry(QtCore.QRect(640, 240, 261, 101))
        self.start_pushButton.setObjectName("start_pushButton")
        self.TimeTable_label = QtWidgets.QLabel(Dialog)
        self.TimeTable_label.setGeometry(QtCore.QRect(30, 90, 101, 16))
        self.TimeTable_label.setObjectName("TimeTable_label")
        self.TimeTable_tableWidget = QtWidgets.QTableWidget(Dialog)
        self.TimeTable_tableWidget.setGeometry(QtCore.QRect(30, 110, 581, 231))
        self.TimeTable_tableWidget.setObjectName("TimeTable_tableWidget")
        self.TimeTable_tableWidget.setColumnCount(3)
        self.TimeTable_tableWidget.setRowCount(15)
        item = QtWidgets.QTableWidgetItem()
        self.TimeTable_tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.TimeTable_tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.TimeTable_tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.TimeTable_tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.TimeTable_tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.TimeTable_tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.TimeTable_tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.TimeTable_tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.TimeTable_tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.TimeTable_tableWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.TimeTable_tableWidget.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.TimeTable_tableWidget.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.TimeTable_tableWidget.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.TimeTable_tableWidget.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.TimeTable_tableWidget.setVerticalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.TimeTable_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.TimeTable_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.TimeTable_tableWidget.setHorizontalHeaderItem(2, item)
        self.ReadQueue_label = QtWidgets.QLabel(Dialog)
        self.ReadQueue_label.setGeometry(QtCore.QRect(30, 360, 101, 16))
        self.ReadQueue_label.setObjectName("ReadQueue_label")
        self.ganttChart_label = QtWidgets.QLabel(Dialog)
        self.ganttChart_label.setGeometry(QtCore.QRect(30, 500, 151, 16))
        self.ganttChart_label.setObjectName("ganttChart_label")
        self.Ganttchart_tableWidget = QtWidgets.QTableWidget(Dialog)
        self.Ganttchart_tableWidget.setGeometry(QtCore.QRect(30, 520, 871, 131))
        self.Ganttchart_tableWidget.setObjectName("Ganttchart_tableWidget")
        self.Ganttchart_tableWidget.setColumnCount(0)
        self.Ganttchart_tableWidget.setRowCount(0)
        self.ResultTable_label = QtWidgets.QLabel(Dialog)
        self.ResultTable_label.setGeometry(QtCore.QRect(30, 660, 121, 16))
        self.ResultTable_label.setObjectName("ResultTable_label")
        self.ResultTable_tableWidget = QtWidgets.QTableWidget(Dialog)
        self.ResultTable_tableWidget.setGeometry(QtCore.QRect(30, 680, 871, 241))
        self.ResultTable_tableWidget.setObjectName("ResultTable_tableWidget")
        self.ResultTable_tableWidget.setColumnCount(6)
        self.ResultTable_tableWidget.setRowCount(14)
        item = QtWidgets.QTableWidgetItem()
        self.ResultTable_tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.ResultTable_tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.ResultTable_tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.ResultTable_tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.ResultTable_tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.ResultTable_tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.ResultTable_tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.ResultTable_tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.ResultTable_tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.ResultTable_tableWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.ResultTable_tableWidget.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.ResultTable_tableWidget.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.ResultTable_tableWidget.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.ResultTable_tableWidget.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.ResultTable_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.ResultTable_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.ResultTable_tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.ResultTable_tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.ResultTable_tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.ResultTable_tableWidget.setHorizontalHeaderItem(5, item)
        self.ReadQueue_tableWidget = QtWidgets.QTableWidget(Dialog)
        self.ReadQueue_tableWidget.setGeometry(QtCore.QRect(30, 380, 871, 111))
        self.ReadQueue_tableWidget.setObjectName("ReadQueue_tableWidget")
        self.ReadQueue_tableWidget.setColumnCount(10)
        self.ReadQueue_tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.ReadQueue_tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.ReadQueue_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.ReadQueue_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.ReadQueue_tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.ReadQueue_tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.ReadQueue_tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.ReadQueue_tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.ReadQueue_tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.ReadQueue_tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.ReadQueue_tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.ReadQueue_tableWidget.setHorizontalHeaderItem(9, item)
        self.AlgorithomList_comboBox = QtWidgets.QComboBox(Dialog)
        self.AlgorithomList_comboBox.setGeometry(QtCore.QRect(33, 50, 101, 31))
        self.AlgorithomList_comboBox.setObjectName("AlgorithomList_comboBox")
        self.AlgorithomList_comboBox.addItem("")
        self.AlgorithomList_comboBox.addItem("")
        self.AlgorithomList_comboBox.addItem("")
        self.AlgorithomList_comboBox.addItem("")
        self.AlgorithomList_comboBox.addItem("")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.AlgorithomList_label.setText(_translate("Dialog", "Algorithom List"))
        self.ProcessName_label.setText(_translate("Dialog", "Process Name"))
        self.ArrivalTime_label.setText(_translate("Dialog", "Arrival Time"))
        self.BurstTime_label.setText(_translate("Dialog", "Burst Time"))
        self.Priority_label.setText(_translate("Dialog", "Priority "))
        self.Add_pushButton.setText(_translate("Dialog", "Add"))
        self.Reset_pushButton.setText(_translate("Dialog", "Reset"))
        self.ProcessNumber_label.setText(_translate("Dialog", "Process Number"))
        self.ExecutionSpeed_label.setText(_translate("Dialog", "Execution Speed"))
        self.RRTimeQuantum_label.setText(_translate("Dialog", "RR Time Quantum"))
        self.label_9.setText(_translate("Dialog", "second(s)"))
        self.label_10.setText(_translate("Dialog", "ms"))
        self.start_pushButton.setText(_translate("Dialog", "START"))
        self.TimeTable_label.setText(_translate("Dialog", "<Time Table>"))
        item = self.TimeTable_tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "1"))
        item = self.TimeTable_tableWidget.verticalHeaderItem(1)
        item.setText(_translate("Dialog", "2"))
        item = self.TimeTable_tableWidget.verticalHeaderItem(2)
        item.setText(_translate("Dialog", "3"))
        item = self.TimeTable_tableWidget.verticalHeaderItem(3)
        item.setText(_translate("Dialog", "4"))
        item = self.TimeTable_tableWidget.verticalHeaderItem(4)
        item.setText(_translate("Dialog", "5"))
        item = self.TimeTable_tableWidget.verticalHeaderItem(5)
        item.setText(_translate("Dialog", "6"))
        item = self.TimeTable_tableWidget.verticalHeaderItem(6)
        item.setText(_translate("Dialog", "7"))
        item = self.TimeTable_tableWidget.verticalHeaderItem(7)
        item.setText(_translate("Dialog", "8"))
        item = self.TimeTable_tableWidget.verticalHeaderItem(8)
        item.setText(_translate("Dialog", "9"))
        item = self.TimeTable_tableWidget.verticalHeaderItem(9)
        item.setText(_translate("Dialog", "10"))
        item = self.TimeTable_tableWidget.verticalHeaderItem(10)
        item.setText(_translate("Dialog", "11"))
        item = self.TimeTable_tableWidget.verticalHeaderItem(11)
        item.setText(_translate("Dialog", "12"))
        item = self.TimeTable_tableWidget.verticalHeaderItem(12)
        item.setText(_translate("Dialog", "13"))
        item = self.TimeTable_tableWidget.verticalHeaderItem(13)
        item.setText(_translate("Dialog", "14"))
        item = self.TimeTable_tableWidget.verticalHeaderItem(14)
        item.setText(_translate("Dialog", "15"))
        item = self.TimeTable_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Process Name"))
        item = self.TimeTable_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Arrival Time(AT)"))
        item = self.TimeTable_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Burst Time(BT)"))
        self.ReadQueue_label.setText(_translate("Dialog", "<Read Queue>"))
        self.ganttChart_label.setText(_translate("Dialog", "<Gantt Chart>"))
        self.ResultTable_label.setText(_translate("Dialog", "<Result Table>"))
        item = self.ResultTable_tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "1"))
        item = self.ResultTable_tableWidget.verticalHeaderItem(1)
        item.setText(_translate("Dialog", "2"))
        item = self.ResultTable_tableWidget.verticalHeaderItem(2)
        item.setText(_translate("Dialog", "3"))
        item = self.ResultTable_tableWidget.verticalHeaderItem(3)
        item.setText(_translate("Dialog", "4"))
        item = self.ResultTable_tableWidget.verticalHeaderItem(4)
        item.setText(_translate("Dialog", "5"))
        item = self.ResultTable_tableWidget.verticalHeaderItem(5)
        item.setText(_translate("Dialog", "6"))
        item = self.ResultTable_tableWidget.verticalHeaderItem(6)
        item.setText(_translate("Dialog", "7"))
        item = self.ResultTable_tableWidget.verticalHeaderItem(7)
        item.setText(_translate("Dialog", "8"))
        item = self.ResultTable_tableWidget.verticalHeaderItem(8)
        item.setText(_translate("Dialog", "9"))
        item = self.ResultTable_tableWidget.verticalHeaderItem(9)
        item.setText(_translate("Dialog", "10"))
        item = self.ResultTable_tableWidget.verticalHeaderItem(10)
        item.setText(_translate("Dialog", "12"))
        item = self.ResultTable_tableWidget.verticalHeaderItem(11)
        item.setText(_translate("Dialog", "13"))
        item = self.ResultTable_tableWidget.verticalHeaderItem(12)
        item.setText(_translate("Dialog", "14"))
        item = self.ResultTable_tableWidget.verticalHeaderItem(13)
        item.setText(_translate("Dialog", "15"))
        item = self.ResultTable_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Process Name"))
        item = self.ResultTable_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Arrival Time(AT)"))
        item = self.ResultTable_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Burst Time(BT)"))
        item = self.ResultTable_tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Wariting Time(WT)"))
        item = self.ResultTable_tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "Turnaround Time(TT)"))
        item = self.ResultTable_tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "Normalized(NTT)"))
        item = self.ReadQueue_tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "Queue"))
        item = self.ReadQueue_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "1"))
        item = self.ReadQueue_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "2"))
        item = self.ReadQueue_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "3"))
        item = self.ReadQueue_tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "4"))
        item = self.ReadQueue_tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "5"))
        item = self.ReadQueue_tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "6"))
        item = self.ReadQueue_tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Dialog", "7"))
        item = self.ReadQueue_tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Dialog", "8"))
        item = self.ReadQueue_tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("Dialog", "9"))
        item = self.ReadQueue_tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("Dialog", "10"))
        self.AlgorithomList_comboBox.setItemText(0, _translate("Dialog", "FCFS"))
        self.AlgorithomList_comboBox.setItemText(1, _translate("Dialog", "RR"))
        self.AlgorithomList_comboBox.setItemText(2, _translate("Dialog", "SPN"))
        self.AlgorithomList_comboBox.setItemText(3, _translate("Dialog", "SRTN"))
        self.AlgorithomList_comboBox.setItemText(4, _translate("Dialog", "HRRN"))
        self.AlgorithomList_comboBox.setItemText(5, _translate("Dialog", "TPFN"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

