import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.QtGui import QIcon

class firstWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(400,500)
        self.setWindowTitle('第一个主窗口应用')
        self.status=self.statusBar()
        self.status.showMessage('只存在5秒钟',5000)

if __name__ == '__main__':
    app=QApplication(sys.argv)
    mainWindow = firstWindow()
    mainWindow.show()
    sys.exit(app.exec_())
