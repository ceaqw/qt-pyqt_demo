# coding: utf8

from PySide2 import QtWidgets, QtCore


class TextWidget(QtWidgets.QWidget):
    def __init__(self):
        super(TextWidget, self).__init__()

        label_name = QtWidgets.QLabel("Name:")
        label_address = QtWidgets.QLabel("Address:")
        self.lineEdit = QtWidgets.QLineEdit()
        self.textEdit = QtWidgets.QTextEdit()

        mainLayout = QtWidgets.QGridLayout()
        mainLayout.addWidget(label_name, 0, 0)
        mainLayout.addWidget(label_address, 1, 0, QtCore.Qt.AlignTop)
        mainLayout.addWidget(self.lineEdit, 0, 1)
        mainLayout.addWidget(self.textEdit, 1, 1)
        self.setLayout(mainLayout)

        self.mainLayout = mainLayout

#
# if __name__ == '__main__':
#     import sys
#     app = QtWidgets.QApplication()
#     ui = TextWidget()
#     ui.show()
#     sys.exit(app.exec_())