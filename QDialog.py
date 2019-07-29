"""
对话框：
QMessageBox
QColorBox
QFontBox
QFileBox
QInputBox

"""
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

class QDiologDemo (QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.setWindowTitle("对话框演示")
        self.resize(300,100)
#不添加布局，直接让按钮显示，要加self//或者self.button=QPushButton("弹出对话框"，self)
        self.button=QPushButton(self)
        self.button.setText("弹出对话框")
        self.button.move(50,50)
        #绑定槽与信号
        self.button.clicked.connect(self.showDiolog)

#新建一个槽
    def showDiolog(self):
        #新建一个对话框
        diolog=QDialog()
        #在对话框里新建一个按钮，继承diolog
        button=QPushButton("确定",diolog)
        #将对话框关闭与按钮点击绑定
        button.clicked.connect(diolog.close)
        button.move(50,50)
        diolog.setWindowTitle('对话框')
        #设置当diolog未关闭时，不可操作主窗口
        diolog.setWindowModality(Qt.ApplicationModal)
        #diolog退出
        diolog.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QDiologDemo()
    main.show()
    sys.exit(app.exec_())

