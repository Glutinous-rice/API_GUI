"""
让控件支持拖拽的动作
A。setDragEnabled(True)
B.setAcceptEvent(True)

B需要两个事件
1.dragEnterEvent   将A拖到B触发
2.dropEvent        将B的区域放下时触发
"""

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


#编写一个类，继承QComboBox属性
class MyComboBox(QComboBox):
    def __init__(self):
        super().__init__()
        self.setAcceptDrops(True)

    def dragEnterEvent(self, e):
        print(e)
        if e.mimeData().hasText():
            e.accept()
        else:
            e.ignore()

    def dropEvent(self,e):
        self.addItem(e.mimeData().text())

           #主类
class  DrapDropDemo(QWidget):
    def __init__(self):
        super().__init__()
        formLayout=QFormLayout()
        formLayout.addRow(QLabel("请将左边的文字拖拽到右边下拉列表中"))
        lineEdit=QLineEdit()
        lineEdit.setDragEnabled(True) #让lineEdit可以拖动
        #创建一个重新定义过的下拉列表
        combo=MyComboBox()
        #将两个控件添加到表单布局
        formLayout.addRow(lineEdit,combo)
        self.setLayout(formLayout)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = DrapDropDemo()
    main.show()
    sys.exit(app.exec_())



