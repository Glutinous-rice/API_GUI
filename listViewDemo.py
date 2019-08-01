from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

class listViewDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.setWindowTitle('QListView例子')
        self.resize(400,500)

        layout=QVBoxLayout()
        #新建一个控件
        listView=QListView(self)
        #建立一个QListView数据源
        listModel=QStringListModel()
        #赋值列表项
        self.list=["列表项1","列表项2","列表项3"]
        #设置数据源的的列表项
        listModel.setStringList(self.list)
        #将数据源添加到控件里
        listView.setModel(listModel)


        #将信号与槽绑定
        listView.clicked.connect(self.clicked)



    def clicked(self,item):
        QMessageBox.information(self,"QListView","您选择了："+self.list[item.row()])








if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = listViewDemo()
    main.show()
    sys.exit(app.exec_())
