"""
输入对话框：QInputDiolog
QInputDiolog.getItem   获取项
QInputDiolog.getText   获取文本
QInputDiolog.getInt    获取整数
"""
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

class QInputDialogDemo (QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.setWindowTitle("输入对话框")
        self.resize(300,100)

        layout= QFormLayout()

        self.button1=QPushButton("获取列表中的项")
        #创建单行文本
        self.lineExid1 = QLineEdit()
        #绑定信号与槽
        self.button1.clicked.connect(self.getIndex)
        #添加控件
        layout.addRow(self.button1,self.lineExid1)

        self.button2 = QPushButton("获取整数")
        self.lineExid2 = QLineEdit()
        self.button2.clicked.connect(self.getInt)
        layout.addRow(self.button2, self.lineExid2)

        self.button3 = QPushButton("获取文本")
        self.lineExid3 = QLineEdit()
        self.button3.clicked.connect(self.getText)
        layout.addRow(self.button3, self.lineExid3)

        self.setLayout(layout)

    def getIndex(self):
        items=("c#","c++","Python","Java")
    # 获得的项   ok键       打开获取项的对话框    标题            提示信息    添加列表项目
        item ,    ok=QInputDialog.getItem(self,"获取列表的项？","选择项目",items)
        #如果有值的话
        if ok and item:
            self.lineExid1.setText(item)


    def getInt(self):
        num, ok = QInputDialog.getInt(self, "获取整数", "输入整数")
        if ok and num:
            self.lineExid2.setText(str(num))

    def getText(self):
        text, ok = QInputDialog.getText(self, "获取文本", "输入数字")
        if ok and text:
            self.lineExid3.setText(text)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QInputDialogDemo()
    main.show()
    sys.exit(app.exec_())
