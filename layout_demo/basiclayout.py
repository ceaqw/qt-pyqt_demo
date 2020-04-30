# encoding: utf8
# describe: 基础的layout布局练习

from PySide2 import QtWidgets
import sys


class Dialog(QtWidgets.QDialog):

    NumButton = 5
    NumLabel = 4

    def __init__(self):
        QtWidgets.QDialog.__init__(self)

        self.createHorizontalGroupBox()
        self.createGridLayout()
        self.createFormLayout()

        buttonBox = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel)

        mainLayout = QtWidgets.QVBoxLayout()

        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

        self.menuBar = QtWidgets.QMenuBar()
        self.fileMenu = QtWidgets.QMenu("File", self)
        self.fileMenu.addAction("Exit").triggered.connect(self.close)
        self.menuBar.addMenu(self.fileMenu)
        mainLayout.setMenuBar(self.menuBar)
        mainLayout.addWidget(self.horizontalGroupBox)
        mainLayout.addWidget(self.gridLayoutGroupBox)
        mainLayout.addWidget(self.formLayoutGroupBox)
        mainLayout.addWidget(buttonBox)
        self.setLayout(mainLayout)

        self.resize(640, 480)
        self.setWindowTitle("Basic Layout")
        self.show()

    def createHorizontalGroupBox(self):
        """
        创建按钮组窗口函数
        :return: None
        """
        self.horizontalGroupBox = QtWidgets.QGroupBox("水平布局")
        layout = QtWidgets.QHBoxLayout()

        for i in range(Dialog.NumButton):
            layout.addWidget(QtWidgets.QPushButton("按钮%d" % i))

        self.horizontalGroupBox.setLayout(layout)

    def createGridLayout(self):
        """
        创建网格布局窗口函数
        :return: None
        """
        self.gridLayoutGroupBox = QtWidgets.QGroupBox("网格布局")
        layout = QtWidgets.QGridLayout()

        bigEdit = QtWidgets.QTextEdit()
        bigEdit.setText("此部件占据所有剩余空间")

        for i in range(Dialog.NumLabel):
            label = QtWidgets.QLabel("label%d:" % i)
            lineText = QtWidgets.QLineEdit()
            layout.addWidget(label, i+1, 0)
            layout.addWidget(lineText, i+1, 1)

        layout.addWidget(bigEdit, 0, 2, Dialog.NumLabel+1, 1)

        layout.setColumnStretch(1, 10)
        layout.setColumnStretch(2, 20)

        self.gridLayoutGroupBox.setLayout(layout)

    def createFormLayout(self):
        """
        创建表单布局函数
        :return: None
        """
        self.formLayoutGroupBox = QtWidgets.QGroupBox("表格布局")
        layout = QtWidgets.QFormLayout()

        combox = QtWidgets.QComboBox()
        for i in range(3):
            combox.addItem("item " + str(i+1))

        spinbox = QtWidgets.QSpinBox()
        spinbox.setValue(5)

        layout.addRow(QtWidgets.QLabel("Line 1:"), QtWidgets.QLineEdit())
        layout.addRow(QtWidgets.QLabel("Line 2"), combox)
        layout.addRow(QtWidgets.QLabel("Line 3:"), spinbox)

        self.formLayoutGroupBox.setLayout(layout)


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    ui = Dialog()
    sys.exit(app.exec_())
