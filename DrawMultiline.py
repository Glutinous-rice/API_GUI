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

class drawPointDemo (QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("在窗口绘制直线")
        self.resize(300, 100)


     #只要窗口部件需要被重绘就被调用。paintEvent
    def paintEvent(self,event):
        #新建一个
        painter=QPainter(self)
        painter.begin(self)
        #设置笔刷样式
        pen=QPen(Qt.red,3,Qt.SolidLine)

        painter.setPen(pen)
        #设置线的坐标
        painter.drawLine(20,40,250,40)

        pen.setStyle(Qt.DashLine)
        painter.setPen(pen)
        painter.drawLine(20,80 , 250, 80)

        pen.setStyle(Qt.DashDotDotLine)
        painter.setPen(pen)
        painter.drawLine(20, 120, 250, 120)

        painter.end()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = drawPointDemo()
    main.show()
    sys.exit(app.exec_())

