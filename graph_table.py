# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test_file.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Table(object):
    def setupUi_table(self, Table, categories, rows):
        self.categories = categories
        self.rows = rows

        Table.setObjectName("Table")
        Table.resize(980, 753)

        self.tableWidget = QtWidgets.QTableWidget(Table)
        self.tableWidget.setGeometry(QtCore.QRect(40, 90, 900, 450))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(len(self.categories))
        self.tableWidget.setRowCount(len(self.rows))
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.setAlternatingRowColors(True)
        header = self.tableWidget.horizontalHeader()

        for i in range(len(self.categories)):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(i, item)
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeToContents)

        for i in range(len(self.rows)):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setVerticalHeaderItem(i, item)

        for i in range(len(self.rows)):
            for j in range(len(self.categories)):
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget.setItem(i, j, item)

        self.label_head = QtWidgets.QLabel(Table)
        self.label_head.setGeometry(QtCore.QRect(40, 10, 900, 100))
        self.label_head.setObjectName("label_head")

        self.horizontalLayoutWidget = QtWidgets.QWidget(Table)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(270, 540, 450, 50))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_save = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_save.setObjectName("pushButton_save")
        self.horizontalLayout.addWidget(self.pushButton_save)
        self.pushButton_delete = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_delete.setObjectName("pushButton_delete")
        self.horizontalLayout.addWidget(self.pushButton_delete)

        self.retranslateUi(Table)
        QtCore.QMetaObject.connectSlotsByName(Table)

    def retranslateUi(self, Table):
        _translate = QtCore.QCoreApplication.translate
        Table.setWindowTitle(_translate("Table", "Dialog"))

        for i in range(len(self.rows)):
            item = self.tableWidget.verticalHeaderItem(i)
            item.setText(_translate("Table", str(i + 1)))

        for i in range(len(self.categories)):
            item = self.tableWidget.horizontalHeaderItem(i)
            item.setText(_translate("Table", self.categories[i]))

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)

        for i in range(len(self.rows)):
            for j in range(len(self.categories)):
                item = self.tableWidget.item(i, j)
                item.setText(_translate("Table", str(self.rows[i][j])))

        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.pushButton_save.setText(_translate("Table", "Сохранить"))
        self.pushButton_delete.setText(_translate("Table", "Удалить"))
        self.label_head.setText(
            _translate("Table", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">"
                                "Вывод данных</span></p></body></html>"))