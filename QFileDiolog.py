"""
QFileDiolog

"""

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

class QFileDialogDemo (QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.setWindowTitle("打开文件")
        self.resize(300,100)
        #新建一个垂直标签
        layout= QVBoxLayout()
        #新建一个按钮
        self.button1=QPushButton("加载图片")
        #绑定信号与槽
        self.button1.clicked.connect(self.loadImage)
        #将按钮1添加到垂直布局里
        layout.addWidget(self.button1)


        self.imageLabel=QLabel()
        layout.addWidget(self.imageLabel)

        self.button2=QPushButton("加载文本文件")
        self.button2.clicked.connect(self.loadText)
        layout.addWidget(self.button2)

        self.contents=QTextEdit()
        layout.addWidget(self.contents)
        #将布局添加到窗口里
        self.setLayout(layout)

    #设置一个槽
    def loadImage(self):
        #      窗口标题    "." 代表程序运行目录             注意这个地方的括号问题(*.jpg *.png)
        fname,_=QFileDialog.getOpenFileName(self,"打开文件",".","图像文件(*.jpg *.png)")
        #设置imageLabel的图片标签
        self.imageLabel.setPixmap(QPixmap(fname))


    def loadText(self):
        #新建一个文件对话框
        diolog=QFileDialog()
        #设置文件对话框弹出的时候显示任何文件，不论是文件夹还是文件
        diolog.setFileMode(QFileDialog.AnyFile)
        #设置文件类型过滤器-----选择文件类型
        diolog.setFilter(QDir.Files)

        if diolog.exec_():
            #得到用户选择的文件名
            filenames=diolog.selectedFiles()
            #   open(path, ‘-模式-‘,encoding=’UTF-8’)
            # 即open(路径+文件名, 读写模式, 编码)  "r":Open text file for reading
            #“a”         以“追加”模式打开， (从 EOF 开始, 必要时创建新文件)
            # “a+”       以”读写”模式打开
            # “ab”       以”二进制 追加”模式打开
            # “ab+”     以”二进制 读写”模式打开
            #
            # “w”     以”写”的方式打开
            # “w+”  以“读写”模式打开
            # “wb”  以“二进制 写”模式打开
            # “wb+”  以“二进制 读写”模式打开
            #
            # “r+”     以”读写”模式打开
            # “rb”     以”二进制 读”模式打开
            # “rb+”    以”二进制 读写”模式打开

            f=open (filenames[0],encoding="utf-8",mode="r")
            #用with，会调用f的colse方法，防止我们读取文件不关闭
            with f:
                #读取文件
                data =f.read()
                #设置TextEdit的内容
                self.contents.setText(data)
        print(filenames[0])
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QFileDialogDemo()
    main.show()
    sys.exit(app.exec_())
