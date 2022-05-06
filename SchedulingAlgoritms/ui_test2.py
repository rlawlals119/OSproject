import sys
from PyQt5.QtWidgets import *


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(3)
        self.tableWidget.setColumnCount(15)
        self.setWindowTitle('LineEdit') 
        self.tableWidget.resize(300, 300) 
        self.tableWidget.move(200, 300)
        self.line_edit = QLineEdit(self) 
        self.line_edit.move(75,75) 
        self.text_label = QLabel(self) 
        self.text_label.move(75, 125) 
        self.text_label.setText('hello world') 
        self.button = QPushButton(self) 
        self.button.move(75, 300) 
        self.button.setText('Get Text') 
        self.button.clicked.connect(self.button_event)

        self.tableWidget.setItem(0, 0, QTableWidgetItem(''))
        self.tableWidget.setItem(0, 1, QTableWidgetItem(''))
        self.tableWidget.setItem(1, 0, QTableWidgetItem(''))
        self.tableWidget.setItem(1, 1, QTableWidgetItem(''))

        layout = QVBoxLayout()
        layout.addWidget(self.tableWidget)
        self.setLayout(layout)

        self.setWindowTitle('PyQt5 - QTableWidget')
        self.setGeometry(300, 500, 600, 400)
        self.show()
    
    def button_event(self): 
        text = self.line_edit.text() # line_edit text 값 가져오기 
        self.tableWidget.setItem(0, 0, QTableWidgetItem(text))

#    def Add_pushButton(self):

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())