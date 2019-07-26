import sys
from PyQt5.QtWidgets import QApplication,QToolTip,QPushButton,QHBoxLayout,QWidget,QMainWindow
from PyQt5.QtGui import QFont
class toolTip (QMainWindow):    #QMainWindow中才有setCentralWidget
    def __init__(self):
        super().__init__()
        self.tip()

    def tip(self):
         QToolTip.setFont(QFont('',22))
         self.setToolTip('今天周五')
         self.setWindowTitle('设置提示信息')
         self.resize(400,500)
         self.button1 = QPushButton('按钮')
         self.button1.setToolTip('这是按钮')
         layout=QHBoxLayout()     #建立水平布局
         layout.addWidget(self.button1)    #将控件添加到布局当中
         mainFrame=QWidget()               #建立一个框架
         mainFrame.setLayout(layout)       #将水平布局添加到框架之中
         self.setCentralWidget(mainFrame)  #将框架添加到窗口当中（将窗口填满）


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main =toolTip()
    main.show()
    sys.exit(app.exec_())

