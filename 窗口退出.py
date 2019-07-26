import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QPushButton,QHBoxLayout,QWidget

class quitAPPlication(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('居中显示')
        self.resize(400,500)
        #添加button
        self.button1= QPushButton('退出应用程序')
        #将信号与槽连接起来
        self.button1.clicked.connect(self.click_quit)
        #创建一个水平布局
        layOut =QHBoxLayout()
        #将button1组件加入到平布局里
        layOut.addWidget(self.button1)
        #创建一个框架
        mainFrame= QWidget()
        #将布局放到框架里
        mainFrame.setLayout(layOut)
        #把框架放到主窗口里
        self.setCentralWidget(mainFrame)

     # 按钮时间的方法（自定义槽）
    def click_quit(self):
        sender=self.sender()
        app=QApplication.instance()
        app.quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main =quitAPPlication ()
    main.show()
    sys.exit(app.exec_())

