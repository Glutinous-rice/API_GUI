"""
日历控件
"""
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

class dateTimeEdit(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.setWindowTitle('多种风格日历显示')
        self.resize(400,500)

        layout=QVBoxLayout()

        dateTimeEdit_1=QDateTimeEdit()
        dateTimeEdit_2=QDateTimeEdit(QDateTime.currentDateTime())

        dateEdit=QDateTimeEdit(QDate.currentDate())
        timeEdit=QDateTimeEdit(QTime.currentTime())

        dateTimeEdit_1.setDisplayFormat("yy-MM-dd HH-mm-ss")
        dateTimeEdit_2.setDisplayFormat("yy/MM/dd  HH/mm/ss")
        dateEdit.setDisplayFormat("yy.MM.dd")
        timeEdit.setDisplayFormat("HH/mm/ss")

        layout.addWidget(dateTimeEdit_1)
        layout.addWidget(dateTimeEdit_2)
        layout.addWidget(dateEdit)
        layout.addWidget(timeEdit)

        self.setLayout(layout)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = dateTimeEdit()
    main.show()
    sys.exit(app.exec_())



"""
DateTime.ToString()的各种日期格式
例：
ToString:2016/9/27 0:00:00
ToString("yyyy/MM/dd"):2016/09/27
ToString("yyyy-MM-dd"):2016-09-27
ToString("yyyy.MM.dd"):2016.09.27
ToString("dd/MM/yyyy"):27/09/2016
ToString("dd-MM-yyyy"):27-09-2016
ToString("yyyy年MM月dd日"):2016年09月27日
"""








