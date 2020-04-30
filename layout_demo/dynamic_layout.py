# coding: utf8

import sys
from PySide2.QtCore import Qt, QSize
from PySide2 import QtWidgets


class MyWidget(QtWidgets.QDialog):
    def __init__(self):
        super(MyWidget, self).__init__()

        self.rotableWidgetList = []

        self.createRotableGroupBox()
        self.createoptionsGroupBox()
        self.createButtonsGroupBox()

        self.mainLayout = QtWidgets.QGridLayout()

        self.mainLayout.addWidget(self.rotableGroupBox, 0, 0)
        self.mainLayout.addWidget(self.optionsGroupBox, 1, 0)
        self.mainLayout.addWidget(self.buttonGroupBox, 2, 0)
        self.setLayout(self.mainLayout)

        self.setWindowTitle("Dynamic Layout")
        self.show()

    def createRotableGroupBox(self):
        """
        创建旋转部件组窗口
        :return:
        """
        self.rotableGroupBox = QtWidgets.QGroupBox("Rotable Widgets")

        self.rotableWidgetList.append(QtWidgets.QSpinBox())
        self.rotableWidgetList.append(QtWidgets.QSlider())
        self.rotableWidgetList.append(QtWidgets.QDial())
        self.rotableWidgetList.append(QtWidgets.QProgressBar())

        count = len(self.rotableWidgetList)
        for i in range(count):
            self.rotableWidgetList[i].valueChanged[int].connect(self.rotableWidgetList[(i+1) % count].setValue)

        self.rotableLayout = QtWidgets.QGridLayout()
        self.rotableGroupBox.setLayout(self.rotableLayout)

        self.rotableWidgets()

    def createoptionsGroupBox(self):
        """
        创建选项组
        :return:
        """
        self.optionsGroupBox = QtWidgets.QGroupBox("Options")

        buttonOrientationLabel = QtWidgets.QLabel("Orientation of buttons:")
        orientationComBox = QtWidgets.QComboBox()
        orientationComBox.addItem("Horizontal", Qt.Horizontal)
        orientationComBox.addItem("Vertical", Qt.Vertical)
        orientationComBox.currentIndexChanged[int].connect(self.buttonOrientationChanged)
        self.orientationComBox = orientationComBox

        layout = QtWidgets.QGridLayout()
        layout.addWidget(buttonOrientationLabel, 0, 0)
        layout.addWidget(orientationComBox, 0, 1)
        layout.setColumnStretch(2, 1)

        self.optionsGroupBox.setLayout(layout)

    def createButtonsGroupBox(self):
        """
        创建按钮组视图
        :return:
        """
        self.buttonGroupBox = QtWidgets.QDialogButtonBox()

        closeButton = self.buttonGroupBox.addButton(QtWidgets.QDialogButtonBox.Close)
        rotableButton = self.buttonGroupBox.addButton("Rotable Widgets", QtWidgets.QDialogButtonBox.ActionRole)

        rotableButton.clicked.connect(self.rotableWidgets)
        closeButton.clicked.connect(self.close)

    def rotableWidgets(self):
        """
        布局旋转函数
        :return:
        """
        count = len(self.rotableWidgetList)

        if count % 2 != 0:
            raise AssertionError("The list's length must be even")

        for widget in self.rotableWidgetList:
            self.rotableLayout.removeWidget(widget)

        self.rotableWidgetList.append(self.rotableWidgetList.pop(0))

        for i in range(count//2):
            self.rotableLayout.addWidget(self.rotableWidgetList[i], i, 0)
            self.rotableLayout.addWidget(self.rotableWidgetList[i+2], i, 1)

    def buttonOrientationChanged(self, index):
        """
        布局方向被改变出发函数
        :return:
        """
        # 取消布局约束
        self.mainLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.setMinimumSize(0, 0)

        orientation = Qt.Orientation(int(self.orientationComBox.itemData(index)))

        self.mainLayout.removeWidget(self.buttonGroupBox)
        spacing = self.mainLayout.spacing()
        oldSizeHint = self.buttonGroupBox.sizeHint() + QSize(spacing, spacing)
        self.buttonGroupBox.setOrientation(orientation)
        newSizeHint = self.buttonGroupBox.sizeHint() + QSize(spacing, spacing)

        if orientation == Qt.Horizontal:
            self.mainLayout.addWidget(self.buttonGroupBox, 2, 0)
            self.resize(self.size() + QSize(-oldSizeHint.width(), newSizeHint.height()))
        else:
            self.mainLayout.addWidget(self.buttonGroupBox, 1, 1, 2, 1)
            self.resize(self.size() + QSize(newSizeHint.width(), -oldSizeHint.height()))


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    ui = MyWidget()
    sys.exit(app.exec_())
