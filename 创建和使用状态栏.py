from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

class statusBarDemo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.setWindowTitle('创建和使用状态栏')
        self.resize(400,500)
        #获取一个菜单栏
        tb1=self.menuBar()
        #向菜单栏添加一个母菜单项
        file=tb1.addMenu('文件')
        #向菜单栏添加一个子菜单项
        file.addAction("show")
        #绑定信号与槽
        file.triggered.connect(self.file_triggered)
        #新建一个状态栏
        self.statusBar=QStatusBar()
        #设置状态栏
        self.setStatusBar(self.statusBar)

     #建立槽，返回来的q,看是哪一个被点击了
    def file_triggered(self,q):
        if q.text()=="show":
            self.statusBar.showMessage(q.text()+"菜单被点击了",5000)







if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = statusBarDemo()
    main.show()
    sys.exit(app.exec_())
