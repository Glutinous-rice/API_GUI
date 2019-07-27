"""
QComboBox下拉列表控件

1.如何将将列表项添加到QComboBox当中
2.如何获取选中的列表项

"""
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

class QComboBoxDemo (QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.setWindowTitle("下拉列表Demo")
        self.resize(100,100)

        layout = QVBoxLayout()

        self.label=QLabel('请选择编程语言')
        self.cb=QComboBox()
        self.cb.addItem("Python")
        self.cb.addItem("C#")
        #一次性添加多个用addItems
        self.cb.addItems(["Java","c++","Goto"])
        # 定义一个事件
        self.cb.currentIndexChanged.connect(self.comboBoxSelectChange)
        #将两个控件添加到布局里
        layout.addWidget(self.label)
        layout.addWidget(self.cb)
        self.setLayout(layout)
     # 这个槽默认传递两个参数，一个是控件本身，一个是索引 ----currentIndexChanged
    def comboBoxSelectChange(self,i):
        # 把当前选中的在label上显示
        self.label.setText(self.cb.currentText())
        # 使之自动调整，根据选中的文本
        self.label.adjustSize()
         #self.cb.count()是总个数
        for count in range(self.cb.count()):
            print("item"+str(count)+"="+self.cb.itemText(count))
        print("current index",i,"selection changed",self.cb.currentText())
        # a=self.cb.count()
        # print(a)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QComboBoxDemo()
    main.show()
    sys.exit(app.exec_())



