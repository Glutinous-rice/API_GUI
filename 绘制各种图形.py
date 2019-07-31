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

class drawAllDemo (QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("在窗口绘制各种图形")
        # self.resize(300, 100)


     #只要窗口部件需要被重绘就被调用。paintEvent
    def paintEvent(self,event):
        #新建一个
        qp=QPainter(self)
        qp.begin(self)

        qp.setPen(Qt.blue)
        #绘制弧
        rect=QRect(0,10,100,100)
           #alen:1个alen等于1/16
        qp.drawArc(rect,0,50*16)

        #椭圆
        qp.drawEllipse(120,120,150,100)

        #绘制五边形
        point1= QPoint(140,380)
        point2= QPoint(270,420)
        point3= QPoint(290,512)
        point4= QPoint(290,588)
        point5= QPoint(200,533)

        polygon=QPolygon([point1,point2,point3,point4,point5])
        qp.drawPolygon(polygon)

        #绘制图像
        image=QImage("./Love.png")
        rect=QRect(10,400,image.width()/3,image.height()/3)
        qp.drawImage(rect,image)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = drawAllDemo()
    main.show()
    sys.exit(app.exec_())

