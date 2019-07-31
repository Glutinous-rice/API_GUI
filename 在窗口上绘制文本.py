'''
绘制API：绘制文本
1.文本
2.各种图形（圆，弧，直线。。。。。）
3.图像

QPainter
painter=QPainter()
painter.begin()
painter.drawText(...)
painter.end()


必须在paintEvent事件方法中绘制各种元素
'''

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

class drawTextDemo (QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("在窗口上绘制文本")
        self.resize(300, 100)
        #设置窗口文字
        self.text="python从菜鸟到高手"

     #定于一个窗口大小改变的事件
    def paintEvent(self,event):
        #新建一个
        painter=QPainter(self)
        painter.begin(self)

        painter.setPen(QColor(150,40,23))
        painter.setFont(QFont("SimSun",25))
        painter.drawText(event.rect(),Qt.AlignCenter,self.text)
        painter.end()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = drawTextDemo()
    main.show()
    sys.exit(app.exec_())

