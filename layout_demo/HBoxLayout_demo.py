# encoding: utf8
# describe: 水平布局示例

from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QMessageBox
import sys


class MyWidget(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        # super(MyWidget, self).__init__()

        self.btn = QPushButton("关闭按钮")
        self.btn_mess = QPushButton("弹窗提示")
        self.btn.clicked.connect(self.close)
        self.btn_mess.clicked.connect(self.mess)
        self.layout = QHBoxLayout()
        self.layout.addWidget(self.btn)
        self.layout.addWidget(self.btn_mess)
        self.setLayout(self.layout)

        self.resize(640, 480)
        self.show()

    def mess(self):
        """
        消息弹窗提示
        :return:
        """
        QMessageBox.information(self, "提示信息", "Hello World!!", QMessageBox.Ok | QMessageBox.Cancel)


if __name__ == '__main__':
    app = QApplication()
    ui = MyWidget()
    sys.exit(app.exec_())
