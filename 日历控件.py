"""
日历控件
"""
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

class MyCalendar(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.setWindowTitle('日历控件演示')
        self.resize(400,500)
        #新建一个日历控件，如果直接要再窗口显示的话，要在后面的括号内加（self）,不然不显示
        self.calendar=QCalendarWidget(self)    #后面的括号里的self必须加
        #设置日历最小时间
        self.calendar.setMinimumDate(QDate(1988,1,1))
        #设置最大时间
        self.calendar.setMaximumDate(QDate(2088,1,1))
        #设置日历的网格可见
        self.calendar.setGridVisible(True)
        #将日历移动到窗口（20，20）处显示
        self.calendar.move(20,20)
        #新建一个标签
        self.label=QLabel(self)
        #将选中的日期传给参数date
        date_1=self.calendar.selectedDate()
        #将日期在标签上显示
        self.label.setText(date_1.toString("yyy-MM-dd dddd"))
        #将信号与槽绑定
        self.calendar.clicked.connect(self.showDate)
        #将标签移动
        self.label.move(20,450)
        #新建一个槽，传入一个date参数
    def showDate(self,date):
        #self.label.setText(date.toString("yy-MM-dd dddd")) #是一种格式，详细见文末
        self.label.setText(self.calendar.selectedDate().toString("yy-MM-dd dddd"))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MyCalendar()
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








