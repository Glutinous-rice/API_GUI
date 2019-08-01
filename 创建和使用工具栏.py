"""
创建和使用工具栏

工具栏默认按钮：只显示图标，将文本作为悬停提示展示
"""
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

class toolBarDemo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.setWindowTitle('创建和使用工具栏')
        self.resize(400,500)
        #新建一个工具栏
        tb1=self.addToolBar("tb1")
        #创建一个file工具， 设置图标/提示文字/parent继承
        file=QAction(QIcon("./DOC.png"),"文件",self)
        #将工具添加到工具栏tb1中
        tb1.addAction(file)

        save=QAction(QIcon("./5f.png"),"储存",self)
        tb1.addAction(save)
        #设置工具栏提示文字的位置
        tb1.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)


        tb2=self.addToolBar("tb2")
        back=QAction(QIcon("./2132.png"),"返回",self)
        tb2.addAction(back)
        tb2.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = toolBarDemo()
    main.show()
    sys.exit(app.exec_())
