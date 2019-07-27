from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

class QRadioButtonDemo (QDialog):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.setWindowTitle("单选按钮")
        self.resize(400,300)

        self .button1=QRadioButton('按钮1')
        #预先设置button1选中
        self.button1.setChecked(True)

        self.button2 = QRadioButton('按钮2')
        #将槽与信号绑定  toggled 切换时触发
        self.button1.toggled.connect(self.toggle_button)
        self.button2.toggled.connect(self.toggle_button)


        Hbox=QHBoxLayout()
        Hbox.addWidget(self.button1)
        Hbox.addWidget(self.button2)
        self.setLayout(Hbox)

    def toggle_button(self):
        #获取当前控件
        radiobutton = self.sender()
        if radiobutton.isChecked() == True:
            print("<"+radiobutton.text()+">被选中")
        else:
            print("<"+radiobutton.text()+">被取消")
        # print(radiobutton.text())



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QRadioButtonDemo ()
    main.show()
    sys.exit(app.exec_())
