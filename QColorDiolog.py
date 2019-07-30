"""
QFontDiolog

"""

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import matplotlib.pyplot as plt # plt 用于显示图片
import matplotlib.image as mpimg # mpimg 用于读取图片
import numpy as np



class QColorDialogDemo (QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.setWindowTitle("颜色对话框")
        self.resize(300,100)

        layout= QVBoxLayout()
        self.button=QPushButton("请选择颜色")
        self.button.clicked.connect(self.set_Color)

        self.label=QLabel('Hello World')

        self.label_image=QLabel()
        #设置label_image的图像为
        self.label_image.setPixmap(QPixmap("./QPalette.png"))

        self.button.setIcon(QIcon("./Love.png"))


        layout.addWidget(self.button)
        layout.addWidget(self.label)
        layout.addWidget(self.label_image)

        self.setLayout(layout)


    def set_Color(self):
        #获取字体对话框的值
        color = QColorDialog.getColor()
        #新建一个调色板
        p= QPalette()
        #设置label的文本的颜色为color
        p.setColor(QPalette.WindowText,color)
        #设置标签的颜色
        self.label.setPalette(p)

        #设置label的背景色为color
        p.setColor(QPalette.Window, color)
        self.label.setPalette(p)
        self.label.setAutoFillBackground(True)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QColorDialogDemo()
    main.show()
    sys.exit(app.exec_())


"""
Qt中提供的调色板QPalette类就是专门用于管理控件的外观显示。QPalette类相当于对话框或控件的调色板，管理着控件和窗体的所有颜色。

每个窗体和控件都包含一个QPalette对象，在显示时，对其做相应的设置即可。
具体看QPalette.png图片
"""