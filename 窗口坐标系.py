import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QPushButton,QHBoxLayout,QWidget
#定义一个槽
def on_Click():
    print('1')
    print('widget.x()=%d' % widget.x())
    print('widget.y()=%d' % widget.y())
    print('widget.width()=%d' % widget.width())
    print('widget.height()=%d' % widget.height())

    print('2')
    print('widget.geometry().x()=%d' % widget.geometry().x())
    print('widget.geometry().y()=%d' % widget.geometry().y())
    print('widget.geometry().width()=%d' % widget.geometry().width())
    print('widget.geometry().height()=%d' % widget.geometry().height())

    print('3')
    print('widget.frameGeometry().x()=%d' % widget.frameGeometry().x())
    print('widget.frameGeometry().y()=%d' % widget.frameGeometry().y())
    print('widget.frameGeometry().width()=%d' % widget.frameGeometry().width())
    print('widget.frameGeometry().height()=%d' % widget.frameGeometry().height())

app=QApplication(sys.argv)  #创建一个应用
widget=QWidget()            #创建一个窗口
btn=QPushButton(widget)     #创建一个按钮，继承widget的类
btn.setText('按钮')         #设置button的文字
btn.move(24,52)             #设置button的位置
btn.clicked.connect(on_Click) #建立槽与信号的关联
widget.resize(300,240)      #设置窗口的大小
widget.move(250,200)
widget.setWindowTitle('屏幕坐标系')
widget.show()               #使窗口显示
sys.exit(app.exec_())       #完美退出





