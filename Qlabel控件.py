# QLabel控件
# setAlignment():  设置文本对齐方式
# setIndent()      设置文本缩进
# text()           获取文本内容
# setBuddy()       设置伙伴关系
# setText()        设置文本内容
# selectedText()   返回所选的字符
# setWordWrap()    设置是否允许换行
#
# QLabel常用的信号（事件）：
# 1.当鼠标滑过QLabel控件的时候触发：linkHovered
# 2.当鼠标单击QLabel控件时触发：linkActivated


import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QWidget,QLabel,QVBoxLayout
from PyQt5.QtGui import QPalette,QPixmap
from PyQt5.QtCore import Qt
class QLabelDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        #添加label控件
        label1= QLabel(self)
        label2= QLabel(self)
        label3= QLabel(self)
        label4= QLabel(self)
        #设置窗口大小
        self.resize(400,500)
        #设置label1的文字及其颜色
        label1.setText("<font color=yellow>这是一个文本标签。</font>")
        #设置label1的自动填充背景
        label1.setAutoFillBackground(True)
        #创建以一个调色板
        Palette=QPalette()
        #设置调色板为绿色
        Palette.setColor(QPalette.Window,Qt.green)
        #对label1设置调色板
        label1.setPalette(Palette)
        #设置label1的文本居中对齐
        label1.setAlignment(Qt.AlignCenter)

        #设置label2的文本
        label2.setText("<a href ='#'>欢迎使用Python  GUI程序</a>")

        #设置标签3居中
        label3.setAlignment(Qt.AlignCenter)
        label3.setToolTip('这是一个图片标签')
        #设置图片标签（路径设置："./路径"）
        label3.setPixmap(QPixmap("./Love.png"))
        # 如果设置为True则用浏览器打开链接；如果设置为Flase则调用槽
        label4.setOpenExternalLinks(True)
        # 设置label4的文本和链接
        label4.setText("<a href = 'https://item.jd.com/12417265.html'>感谢关注《Python从菜鸟到大神》<./a>")
        label4.setAlignment(Qt.AlignLeft)
        label4.setToolTip('这是一个超级链接')
        # 新建一个垂直布局
        Vbox=QVBoxLayout()
        # 向布局里添加控件
        Vbox.addWidget(label1)
        Vbox.addWidget(label2)
        Vbox.addWidget(label3)
        Vbox.addWidget(label4)

        self.setLayout(Vbox)
        self.setWindowTitle('Label控件演示')

        #设置槽
        label2.linkHovered.connect(self.linkHovered)
        label4.linkActivated.connect(self.linkClicked)





    def linkHovered(self):
        print('当鼠标滑过Label2标签，触发事件')

    def linkClicked(self):
        print('当鼠标单击Label4标签，触发事件')







if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QLabelDemo()
    main.show()
    sys.exit(app.exec_())
