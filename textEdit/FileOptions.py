# coding: utf8

from PySide2 import QtWidgets


class SortedDict(dict):
    class Iterator(object):
        def __init__(self, sorted_dict):
            self._dict = sorted_dict
            self._keys = sorted(self._dict.keys())
            self._nr_items = len(self._keys)
            self._idx = 0

        def __iter__(self):
            return self

        def next(self):
            if self._idx >= self._nr_items:
                raise StopIteration

            key = self._keys[self._idx]
            value = self._dict[key]
            self._idx += 1

            return key, value

        __next__ = next

    def __iter__(self):
        return SortedDict.Iterator(self)

    iterkeys = __iter__


class FileOptions(QtWidgets.QWidget):
    def __init__(self):
        super(FileOptions, self).__init__()

        btn = QtWidgets.QPushButton("保存")
        btn.clicked.connect(self.Save)
        btn1 = QtWidgets.QPushButton("读取")
        btn1.clicked.connect(self.Read)

        mainLayout = QtWidgets.QHBoxLayout()
        mainLayout.addWidget(btn)
        mainLayout.addWidget(btn1)
        self.setLayout(mainLayout)

    def Save(self):
        fileName,_ = QtWidgets.QFileDialog.getSaveFileName(self, "Save 11", '', "All Files(*)")

        fp = open(str(fileName), "w")

        fp.write("13131651651132")
        fp.close()

        QtWidgets.QMessageBox.information(self, "提示", "保存成功")

    def Read(self):
        fileName,_ = QtWidgets.QFileDialog.getOpenFileName(self, "打开", "", "文本文件 (*.txt)")

        fp = open(str(fileName), 'r')
        print(fp.read())
        fp.close()
        QtWidgets.QMessageBox.information(self, "提示", "加载成功")


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication()
    ui = FileOptions()
    ui.show()
    sys.exit(app.exec_())
