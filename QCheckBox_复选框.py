""""
复选框
未选中   0
半选中   1
选中     2

"""
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

class QCheckBoxDemo (QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.setWindowTitle("复选框")
        self.resize(400,300)

        layout =QHBoxLayout()

        self.checkbox1=QCheckBox("复选框1")
        self.checkbox1.setChecked(True)
        self.checkbox1.stateChanged.connect(lambda:self.checkboxState(self.checkbox1))
        layout.addWidget(self.checkbox1)

        self.checkbox2=QCheckBox("复选框2")
        self.checkbox2.stateChanged.connect(lambda:self.checkboxState(self.checkbox2))
        layout.addWidget(self.checkbox2)

        self.checkbox3=QCheckBox("半选中")
        #这边使用了lambda函数，所以在定义槽的时候，需要多加一个参数，不然会报错
        self.checkbox3.stateChanged.connect(lambda:self.checkboxState(self.checkbox3))
        #下面两个语句是半选中必须要设置的
        self.checkbox3.setTristate(True)
        self.checkbox3.setCheckState(Qt.PartiallyChecked)
        #将checkbox3控件加入水平布局当中
        layout.addWidget(self.checkbox3)
        #把水平布局加入到窗口里
        self.setLayout(layout)


        # 设置一个槽，与之对应的，checkboxState函数必须要有两个参数，不然会报错
    def checkboxState(self,cb):
        check1Status = self.checkbox1.text()+",isChecked="+str(self.checkbox1.isChecked())+",checkState="+str(self.checkbox1.checkState())+"\n"
        check2Status = self.checkbox2.text()+",isChecked="+str(self.checkbox2.isChecked())+",checkState="+str(self.checkbox2.checkState())+"\n"
        check3Status = self.checkbox3.text()+",isChecked="+str(self.checkbox3.isChecked())+",checkState="+str(self.checkbox3.checkState())+"\n"
        print(check1Status+check2Status+check3Status)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QCheckBoxDemo()
    main.show()
    sys.exit(app.exec_())
