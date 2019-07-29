"""
消息对话框：QMessageBox
1.关于对话框
2.错误对话框
3.警告对话框
4.提问对话框
5.消息对话框

2点差异：
1.显示的对话框图标不一样
2.显示的按钮不一样

"""

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

#类名千万不要和函数名重复！
class QMessageBoxDemo (QWidget):
    def __init__(self):
        super(QMessageBoxDemo,self).__init__()
        self.initUi()

    def initUi(self):
        self.setWindowTitle("对话框演示")
        self.resize(300,100)
        #创建一个布局
        layout= QVBoxLayout()
        #新建一个按钮，并设置显示内容
        self.button1=QPushButton("显示关于对话框")
        #绑定信号与槽
        self.button1.clicked.connect(self.showDiolog)

        self.button2 = QPushButton("显示错误对话框")
        self.button2.clicked.connect(self.showDiolog)

        self.button3 = QPushButton("显示警告对话框")
        self.button3.clicked.connect(self.showDiolog)

        self.button4 = QPushButton("显示提问对话框")
        self.button4.clicked.connect(self.showDiolog)

        self.button5 = QPushButton("显示消息对话框")
        self.button5.clicked.connect(self.showDiolog)


        #把控件添加到布局里
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)
        layout.addWidget(self.button4)
        layout.addWidget(self.button5)
        #把布局添加到窗口里，这时。class(Qwidget)
        self.setLayout(layout)


    def showDiolog(self):
        text = self.sender().text()
        if text == '显示关于对话框':
            QMessageBox.about(self,'关于','这是一个关于对话框')
        elif text=="显示错误对话框":
            #后面的critical要小写        标题     显示的内容        代表两个选项，                 最后的代表默认的
            QMessageBox.critical(self, '错误', '这是一个错误对话框',QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
        elif text == "显示警告对话框":
            QMessageBox.warning(self, '警告', '这是一个警告对话框')
        elif text == "显示提问对话框":
            QMessageBox.question(self, '提问', '这是一个提问对话框')
        elif text == "显示消息对话框":
            QMessageBox.information(self, '消息', '这是一个消息对话框')






if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QMessageBoxDemo()
    main.show()
    sys.exit(app.exec_())
