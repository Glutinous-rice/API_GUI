"""
显示二维数据表 （QTableView控件）

数据源:model

需要创建QTableView实例和一个数据源（model），然后将他们链接
"""



from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

class tableView(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.setWindowTitle('显示二维数据表')
        self.resize(400,500)
        #创建一个数据模型
        self.model=QStandardItemModel(4,3)
        #给数据模型设置标签
        self.model.setHorizontalHeaderLabels(["ID","姓名","年龄"])
        #创建一个控件
        self.tableview=QTableView()
        #将控件和model链接起来
        self.tableview.setModel(self.model)

        #添加数据
        item11=QStandardItem("10")
        item12=QStandardItem("雷神")
        item13=QStandardItem("10000")
        self.model.setItem(0,0,item11)
        self.model.setItem(0,1,item12)
        self.model.setItem(0,2,item13)

        item21 = QStandardItem("6")
        item22 = QStandardItem("死亡女神")
        item23 = QStandardItem("1800")
        self.model.setItem(2, 0, item21)
        self.model.setItem(2, 1, item22)
        self.model.setItem(2, 2, item23)


        layout=QVBoxLayout()
        layout.addWidget(self.tableview)
        self.setLayout(layout)













if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = tableView()
    main.show()
    sys.exit(app.exec_())
