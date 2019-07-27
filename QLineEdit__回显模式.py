# """lineEdit与回显模式
# 基本功能：输入单行文本
#  EchoMode（回显模式）
#   四种回显模式
#   1.Normal    输入什么显示什么
#   2.NoEcho    输入什么都不显示
#   3.PassWord   输入什么都显示小圆点
#   4.PassWordEchoOnEdit  输入时显示，不输入时，变成小圆点
#
#
# """
from PyQt5.QtWidgets import *
import sys

class QLineEditEchoMode(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()


    def initUi (self):
        #创建表单布局
        frameLayout =QFormLayout()
        self.resize(400,500)
        #创建四种回显模式的文本行
        NormalQLineEdit = QLineEdit()
        NoEchoQLineEdit = QLineEdit()
        PassWordQLineEdit = QLineEdit()
        PassWordEchoOnEdit = QLineEdit()

        #将控件添加到表单布局里
        #def addRow(self, label: QWidget, field: QWidget) -> None: ...
        #addRow是QFormLayout独有的函数，label在表单布局左边
        frameLayout.addRow('Normal ',NormalQLineEdit)
        frameLayout.addRow('NoEcho ',NoEchoQLineEdit)
        frameLayout.addRow('PassWord ', PassWordQLineEdit)
        frameLayout.addRow('PassWordEchoOnEdit ',PassWordEchoOnEdit)

        #把布局加入到窗口里
        self.setLayout(frameLayout)

        #设置文本行的属性
        NormalQLineEdit.setEchoMode(QLineEdit.Normal)
        NoEchoQLineEdit.setEchoMode(QLineEdit.NoEcho)
        PassWordQLineEdit.setEchoMode(QLineEdit.Password)
        PassWordEchoOnEdit.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        #输入时的灰色提示字
        NormalQLineEdit.setPlaceholderText("Normal")
        NoEchoQLineEdit.setPlaceholderText("NoEcho")
        PassWordQLineEdit.setPlaceholderText("Password")
        PassWordEchoOnEdit.setPlaceholderText("PasswordEchoOnEdit")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main =QLineEditEchoMode()
    main.show()
    sys.exit(app.exec_())

