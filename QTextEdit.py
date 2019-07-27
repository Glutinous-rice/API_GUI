""""
QTextEdit控件

"""
from PyQt5.QtWidgets import *
import sys

class QTextEditDemo (QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.setWindowTitle('QTextEdit控件')
        self.resize(400,300)
        #新建textEdit
        self.textEdit=QTextEdit()
        #设置两个按钮
        self.buttonText= QPushButton('显示文本')
        self.buttonHTML=QPushButton("显示HTML")
        #新建一个垂直布局
        Vbox=QVBoxLayout()
        #把控件添加到布局里
        Vbox.addWidget(self.textEdit)
        Vbox.addWidget(self.buttonText)
        Vbox.addWidget(self.buttonHTML)
        #把布局添加到窗口里
        self.setLayout(Vbox)
        #把槽和信号绑定到一起
        self.buttonText.clicked.connect(self.onclick_buttonText)
        self.buttonHTML.clicked.connect(self.onclick_buttonHTML)
        #设置两个槽
    def onclick_buttonText(self):
        self.textEdit.setPlainText('Hello World  Are you ok?')
                        #获取textEdit的文本用toPlainText
    def onclick_buttonHTML(self):
        self.textEdit.setHtml('<font color="green" size="5">Hello World</font>')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QTextEditDemo()
    main.show()
    sys.exit(app.exec_())
