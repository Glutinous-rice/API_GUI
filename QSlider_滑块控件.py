"""
    QSlider 滑块控件
"""
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

class QSliderDemo (QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.setWindowTitle("滑块控件")
        self.resize(300,300)

        layout = QVBoxLayout()

        self.label=QLabel('你好 Python')
        #设置label的文本居中显示
        self.label.setAlignment(Qt.AlignCenter)
        #将label添加到布局里
        layout.addWidget(self.label)
        #将布局添加到窗口里
        self.setLayout(layout)
        #设置滑块是水平的
        self.slider=QSlider(Qt.Horizontal)

        #设置最大值
        self.slider.setMaximum(100)
        # 设置最小值
        self.slider.setMinimum(0)
        # 设置步长
        self.slider.setSingleStep(2)
        # 设置初始值
        self.slider.setValue(10)
        # 设置刻度位置。刻度在下方
        self.slider.setTickPosition(QSlider.TicksBelow)
        # 设置刻度间隔
        self.slider.setTickInterval(6)

        self.slider.valueChanged.connect(self.valueChange)
        layout.addWidget(self.slider)
        self.setLayout(layout)

    def valueChange(self):
        print("当前值：%s" %self.slider.value())
        #获取当前值
        size = self.slider.value()

        self.label.setFont(QFont("Arial",size))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QSliderDemo()
    main.show()
    sys.exit(app.exec_())
