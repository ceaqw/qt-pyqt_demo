# coding: utf8

from PySide2 import QtWidgets, QtCore
from textEdit.textwidget import TextWidget


class GetText(TextWidget):
    def __init__(self):
        super(GetText, self).__init__()

        self.lineEdit.setEnabled(False)
        self.textEdit.setEnabled(False)

        self.addBtn = QtWidgets.QPushButton("Add")
        self.addBtn.clicked.connect(self.addContact)
        self.submitBtn = QtWidgets.QPushButton("Submit")
        self.submitBtn.clicked.connect(self.submitContact)
        self.submitBtn.hide()
        self.cancelBtn = QtWidgets.QPushButton("Cancel")
        self.cancelBtn.clicked.connect(self.cancelContact)
        self.cancelBtn.hide()

        self.btnLayout = QtWidgets.QVBoxLayout()
        self.btnLayout.addWidget(self.addBtn)
        self.btnLayout.addWidget(self.submitBtn)
        self.btnLayout.addWidget(self.cancelBtn)
        self.mainLayout.addLayout(self.btnLayout, 1, 2, QtCore.Qt.AlignBottom)

    def addContact(self):
        """
        添加文本数据
        :return:
        """
        self.submitBtn.show()
        self.cancelBtn.show()
        self.lineEdit.setEnabled(True)
        self.lineEdit.setFocus(QtCore.Qt.OtherFocusReason)
        self.textEdit.setEnabled(True)
        self.lineEdit.clear()
        self.textEdit.clear()
        self.addBtn.setEnabled(False)

    def submitContact(self):
        """
        提交添加
        :return:
        """
        line_str = self.lineEdit.text()
        text_str = self.textEdit.toPlainText()
        self.lineEdit.setEnabled(False)
        self.textEdit.setEnabled(False)
        self.submitBtn.hide()
        self.cancelBtn.hide()
        # self.textEdit.setToolTip("当前为只读模式")
        self.addBtn.setEnabled(True)
        print(line_str, text_str)

    def cancelContact(self):
        """
        取消提交
        :return:
        """
        self.lineEdit.clear()
        self.textEdit.clear()
        self.lineEdit.setEnabled(False)
        self.textEdit.setEnabled(False)
        self.addBtn.setEnabled(True)
        self.submitBtn.hide()
        self.cancelBtn.hide()


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication()
    ui = GetText()
    ui.show()
    sys.exit(app.exec_())
