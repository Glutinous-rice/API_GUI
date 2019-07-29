"""
QFontDiolog

"""

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

class QFontDialogDemo (QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.setWindowTitle("字体对话框")
        self.resize(300,100)

        layout= QVBoxLayout()
        self.button=QPushButton("请选择字体")
        self.button.clicked.connect(self.chooseFont)

        self.label=QLabel('Hello World')

        layout.addWidget(self.button)
        layout.addWidget(self.label)
        self.setLayout(layout)

    def chooseFont(self):
        #获取字体对话框的值
        font,ok =QFontDialog.getFont()
        #设置标签的字体
        self.label.setFont(font)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QFontDialogDemo()
    main.show()
    sys.exit(app.exec_())
