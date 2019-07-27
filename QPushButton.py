from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

class QPushButtonDemo (QDialog):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.setWindowTitle("按钮控件")
        self.resize(400,300)

        layout =QVBoxLayout()
        self.button1=QPushButton("按钮一")
        # self.button1.setText()
        layout.addWidget(self.button1)
        self.setLayout(layout)
        #据说一下两个是搭配使用的，具体用法还不是很清楚
        # self.button1.setCheckable(True)
        # self.button1.toggle()


        #如下用到了lambda函数，用法也不是很清楚，只知道能把button1和btn联系起来
        self.button1.clicked.connect(lambda :self.onclick_button1(self.button1))

     #定义多加了一个btn参数
    def onclick_button1(self,btn):
        print("被单击按钮是<"+btn.text()+">")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QPushButtonDemo ()
    main.show()
    sys.exit(app.exec_())
