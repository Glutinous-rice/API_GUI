import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QDesktopWidget

class centerfrom(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('居中显示')
        self.resize(400,500)
        self.center()    #调用

    def center(self):
        center = QDesktopWidget().screenGeometry()  #此处括号不能少，少了会出错
        size = self.geometry()

        newLeft = (center.width()-size.width())/2
        newTop = (center.height()-size.height())/2
        self.move(newLeft,newTop)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = centerfrom()
    main.show()
    sys.exit(app.exec_())

