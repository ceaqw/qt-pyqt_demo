# coding: utf8
# describe: win文本编辑窗口

from PySide2 import QtGui, QtCore, QtWidgets, QtPrintSupport


class MyWidget(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWidget, self).__init__()

        self.textEdit = QtWidgets.QTextEdit()
        self.setCentralWidget(self.textEdit)

        self.createActions()
        self.createMenus()
        self.createToolBar()
        self.createDockWindows()

        self.resize(640, 480)
        self.setWindowTitle("Dock Widget")
        self.show()

    def newLeftter(self):
        """
        创建新的信件
        :return:
        """
        self.textEdit.clear()

        cursor = self.textEdit.textCursor()
        cursor.movePosition(QtGui.QTextCursor.Start)
        topFrame = cursor.currentFrame()
        topFrameFormat = topFrame.frameFormat()
        topFrameFormat.setPadding(16)
        topFrame.setFrameFormat(topFrameFormat)

        textFormat = QtGui.QTextCharFormat()
        boldFormat = QtGui.QTextCharFormat()
        boldFormat.setFontPointSize(16)
        boldFormat.setFontWeight(QtGui.QFont.Bold)
        italicFormat = QtGui.QTextCharFormat()
        italicFormat.setFontItalic(True)

        tableFormat = QtGui.QTextTableFormat()
        tableFormat.setBorder(1)
        tableFormat.setCellPadding(16)
        tableFormat.setAlignment(QtGui.Qt.AlignRight)
        cursor.insertTable(1, 1, tableFormat)
        cursor.insertText("The Firm", boldFormat)
        cursor.insertBlock()
        cursor.insertText("This is city street", textFormat)
        cursor.insertBlock()
        cursor.insertText("This is test text area", textFormat)
        cursor.setPosition(topFrame.lastPosition())
        cursor.insertText(QtCore.QDate.currentDate().toString("d MMMM yyyy"), textFormat)

    def _print(self):
        """
        打印信件函数
        :return:
        """
        document = self.textEdit.document()
        printer = QtPrintSupport.QPrinter()

        dlg = QtPrintSupport.QPrintDialog(printer, self)
        if dlg.exec_() != QtWidgets.QDialog.Accepted:
            return

        document.print_(printer)
        self.statusBar().showMessage("Ready", 2000)

    def save(self):
        """
        信封保存函数
        :return:
        """
        fileName, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Choose a file name", ".", "HTML (*.html *.htm)")

        if not fileName:
            return

        file = QtCore.QFile(fileName)
        if not file.open(QtCore.QFile.WriteOnly | QtCore.QFile.Text):
            QtWidgets.QMessageBox.warning(self, "Dock Widgets", "Cannot write file %s:\n%s." % (fileName, file.errorString()))
            return

        out = QtCore.QTextStream(file)
        QtWidgets.QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
        out << self.textEdit.toHtml()
        QtWidgets.QApplication.restoreOverrideCursor()

        self.statusBar().showMessage("Saved %s" % fileName, 2000)

    def undo(self):
        """
        撤销
        :return:
        """
        document = self.textEdit.document()
        document.undo()

    def insertCustomer(self, customer):
        if not customer:
            return
        customerList = customer.split(', ')
        document = self.textEdit.document()
        cursor = document.find('NAME')
        if not cursor.isNull():
            cursor.beginEditBlock()
            cursor.insertText(customerList[0])
            oldcursor = cursor
            cursor = document.find('ADDRESS')
            if not cursor.isNull():
                for i in customerList[1:]:
                    cursor.insertBlock()
                    cursor.insertText(i)
                cursor.endEditBlock()
            else:
                oldcursor.endEditBlock()

    def addParagraph(self, paragraph):
        if not paragraph:
            return
        document = self.textEdit.document()
        cursor = document.find("Yours sincerely,")
        if cursor.isNull():
            return
        cursor.beginEditBlock()
        cursor.movePosition(QtGui.QTextCursor.PreviousBlock, QtGui.QTextCursor.MoveAnchor,
                            2)
        cursor.insertBlock()
        cursor.insertText(paragraph)
        cursor.insertBlock()
        cursor.endEditBlock()

    def createActions(self):
        """
        创建动作
        :return:
        """
        self.newLeftterAct = QtWidgets.QAction(QtGui.QIcon("./images/new.png"), "New Letter", self, shortcut=QtGui.QKeySequence.New, triggered=self.newLeftter)
        self.saveAct = QtWidgets.QAction(QtGui.QIcon("./images/save.png"), "Save", self, shortcut=QtGui.QKeySequence.Save, triggered=self.save)
        self.printAct = QtWidgets.QAction(QtGui.QIcon.fromTheme("document-print", QtGui.QIcon("./images/print.png")), "Print", self, shortcut=QtGui.QKeySequence.Print, triggered=self._print)
        self.quitAct = QtWidgets.QAction("Quit", self, shortcut="Ctrl+Q", statusTip="Quit the application", triggered=self.close)

        self.undoAct = QtWidgets.QAction(QtGui.QIcon("./images/undo.png"), "撤销", self, shortcut=QtGui.QKeySequence.Undo, triggered=self.undo)

        self.aboutAct = QtWidgets.QAction("&About", self, triggered=self.about, shortcut="Ctrl+H")

    def createMenus(self):
        """
        创建主菜单
        :return:
        """
        fileMenu = self.menuBar().addMenu("&File")
        fileMenu.addAction(self.newLeftterAct)
        fileMenu.addAction(self.saveAct)
        fileMenu.addAction(self.printAct)
        # 添加横线
        fileMenu.addSeparator()
        fileMenu.addAction(self.quitAct)
        self.fileMenu = fileMenu

        editMenu = self.menuBar().addMenu("&Edit")
        editMenu.addAction(self.undoAct)
        self.editMenu = editMenu

        self.viewMenu = self.menuBar().addMenu("&View")

        helpMenu = self.menuBar().addMenu("&Help")
        helpMenu.addAction(self.aboutAct)

    def createToolBar(self):
        """
        pass
        :return:
        """
        fileToolBar = self.addToolBar("File")
        fileToolBar.addAction(self.newLeftterAct)
        fileToolBar.addAction(self.saveAct)
        fileToolBar.addAction(self.printAct)
        self.fileToolBar = fileToolBar

        editToolBar = self.addToolBar("Edit")
        editToolBar.addAction(self.undoAct)
        self.editToolBar = editToolBar

    def about(self):
        QtWidgets.QMessageBox.information(self, "关于", "The <b>Dock Widgets</b> example demonstrates how to use "
    "Qt's dock widgets. You can enter your own text, click a "
    "customer to add a customer name and address, and click "
    "standard paragraphs to add them.")

    def createDockWindows(self):
        dock = QtWidgets.QDockWidget("Customers", self)
        dock.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea | QtCore.Qt.RightDockWidgetArea)
        self.customerList = QtWidgets.QListWidget(dock)
        self.customerList.addItems((
            "John Doe, Harmony Enterprises, 12 Lakeside, Ambleton",
            "Jane Doe, Memorabilia, 23 Watersedge, Beaton",
            "Tammy Shea, Tiblanka, 38 Sea Views, Carlton",
            "Tim Sheen, Caraba Gifts, 48 Ocean Way, Deal",
            "Sol Harvey, Chicos Coffee, 53 New Springs, Eccleston",
            "Sally Hobart, Tiroli Tea, 67 Long River, Fedula"))
        dock.setWidget(self.customerList)
        self.addDockWidget(QtCore.Qt.RightDockWidgetArea, dock)
        self.viewMenu.addAction(dock.toggleViewAction())

        dock = QtWidgets.QDockWidget("Paragraphs", self)
        self.paragraphsList = QtWidgets.QListWidget(dock)
        self.paragraphsList.addItems((
            "Thank you for your payment which we have received today.",
            "Your order has been dispatched and should be with you within "
            "28 days.",
            "We have dispatched those items that were in stock. The rest of "
            "your order will be dispatched once all the remaining items "
            "have arrived at our warehouse. No additional shipping "
            "charges will be made.",
            "You made a small overpayment (less than $5) which we will keep "
            "on account for you, or return at your request.",
            "You made a small underpayment (less than $1), but we have sent "
            "your order anyway. We'll add this underpayment to your next "
            "bill.",
            "Unfortunately you did not send enough money. Please remit an "
            "additional $. Your order will be dispatched as soon as the "
            "complete amount has been received.",
            "You made an overpayment (more than $5). Do you wish to buy more "
            "items, or should we return the excess to you?"))
        dock.setWidget(self.paragraphsList)
        self.addDockWidget(QtCore.Qt.RightDockWidgetArea, dock)
        self.viewMenu.addAction(dock.toggleViewAction())

        self.customerList.currentTextChanged.connect(self.insertCustomer)
        self.paragraphsList.currentTextChanged.connect(self.addParagraph)


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication()
    ui = MyWidget()
    sys.exit(app.exec_())