"""
QPainter
painter=QPainter()
painter.begin()
painter.drawText(...)
painter.end()

固定格式
"""
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys,math

class fillRectDemo (QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("在窗口绘制各种图形")
        # self.resize(300, 100)


     #只要窗口部件需要被重绘就被调用。paintEvent
    def paintEvent(self,event):
        #新建一个
        qp=QPainter(self)
        qp.begin(self)
        #设置笔刷的样式
        brush=QBrush(Qt.SolidPattern)
        #设置笔刷
        qp.setBrush(brush)
        #指定填充的区域
        qp.drawRect(10,15,90,60)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = fillRectDemo()
    main.show()
    sys.exit(app.exec_())

