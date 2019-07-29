"""
QSpinBox 计数器

查看更多函数，按住Ctrl键点击QSpinBox
"""
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

class QSpinBoxDemo (QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.setWindowTitle("滑块控件")
        self.resize(300,100)
        #新建一个垂直布局
        layout = QVBoxLayout()
        #新建一个label控件
        self.label=QLabel('当前值：')
        #设置label控件文本属性：居中
        self.label.setAlignment(Qt.AlignCenter)
        #把label控件添加到布局里、
        layout.addWidget(self.label)
        #新建一个计数器
        self.spinBox=QSpinBox()
        #设置计数器的区间
        self.spinBox.setRange(1,42)
        #设置计数器的初始值
        self.spinBox.setValue(10)
        #设置计数器的步长
        self.spinBox.setSingleStep(2)
        #将计数器添加到布局里
        layout.addWidget(self.spinBox)
         #绑定信号与槽
        self.spinBox.valueChanged.connect(self.valueChange)
        #将布局添加到窗口里
        self.setLayout(layout)
    #定义一个槽
    def valueChange(self):
        self.label.setText("当前值："+str(self.spinBox.value()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QSpinBoxDemo()
    main.show()
    sys.exit(app.exec_())
