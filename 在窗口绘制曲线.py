
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys,math

class drawPointDemo (QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("在窗口上绘制2个周期的正弦曲线")
        self.resize(300, 100)


     #定于一个窗口大小改变的事件
    def paintEvent(self,event):
        #新建一个
        painter=QPainter(self)
        painter.begin(self)
        painter.setPen(Qt.blue)
        size=self.size()
        for i in range(1000):
            x=100*(-1+2.0*i/1000)+size.width()/2.0
            y=-50*math.sin((x-size.width()/2.0)*math.pi/50)+size.height()/2.0
            painter.drawPoint(x,y)
        painter.end()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = drawPointDemo()
    main.show()
    sys.exit(app.exec_())

