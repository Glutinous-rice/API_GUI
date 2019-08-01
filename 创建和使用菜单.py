from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

class MenuDemo(QMainWindow):
    def __init__(self):
        super().__init__()
        #获取一个菜单栏
        bar=self.menuBar()
        #新建一个菜单选项
        file=bar.addMenu("文件")
        "方式一"
        #新建一个file的子菜单
        file.addAction("新建")

        quit=QAction("quit",self)   #需要加self
        file.addAction(quit)
        quit.triggered.connect(self.process)

        "方式二"
        #通过QAction新建另一个菜单选项
        save=QAction('保存',self)
        #设置菜单的快捷键
        save.setShortcut("Ctrl+s")
        #将save添加到file菜单里
        file.addAction(save)

        #新建另一个母菜单选项
        edit=bar.addMenu("编辑")
        #添加子菜单选项
        edit.addAction('copy')
        edit.addAction("paste")



    def process(self):
        self.close()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MenuDemo()
    main.show()
    sys.exit(app.exec_())

