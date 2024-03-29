# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'proj.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog, categories, values):
        self.categories = categories
        self.values = values
        self.boxes = []
        self.labels = []
        self.horizontals = []

        for i in range(len(self.categories)):
            self.boxes.append(0)
            self.labels.append(0)
            self.horizontals.append(0)

        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 600)
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(140, 60, 502, 382))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        for i in range(len(self.categories)):
            self.horizontals[i] = QtWidgets.QHBoxLayout()
            self.horizontals[i].setObjectName("horizontalLayout_{}".format(i))
            self.labels[i] = QtWidgets.QLabel(self.verticalLayoutWidget)
            self.labels[i].setObjectName("label_{}".format(i))
            self.horizontals[i].addWidget(self.labels[i])
            self.boxes[i] = QtWidgets.QComboBox(self.verticalLayoutWidget)
            self.boxes[i].setEditable(False)
            self.boxes[i].setCurrentText("")
            self.boxes[i].setObjectName("comboBox_{}".format(i))

            for _ in range(len(self.values[i]) + 1):
                self.boxes[i].addItem("")

            self.horizontals[i].addWidget(self.boxes[i])
            self.verticalLayout.addLayout(self.horizontals[i])

        self.horizontalLayout_last = QtWidgets.QHBoxLayout()
        self.horizontalLayout_last.setObjectName("horizontalLayout_last")
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setEnabled(True)
        self.pushButton.setIconSize(QtCore.QSize(16, 16))
        self.pushButton.setCheckable(False)
        self.pushButton.setChecked(False)
        self.pushButton.setAutoDefault(True)
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_last.addWidget(self.pushButton)

        self.label_last = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_last.setText("")
        self.label_last.setObjectName("label_last")
        self.horizontalLayout_last.addWidget(self.label_last)

        self.combobox_choose_cat = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.combobox_choose_cat.setEditable(False)
        self.combobox_choose_cat.setCurrentText("")
        self.combobox_choose_cat.setObjectName("comboBox_choose_cat")
        for _ in range(len(self.categories)):
            self.combobox_choose_cat.addItem("")
        self.horizontalLayout_last.addWidget(self.combobox_choose_cat)

        self.verticalLayout.addLayout(self.horizontalLayout_last)

        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit.setMouseTracking(False)
        self.verticalLayout.addWidget(self.plainTextEdit)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))

        for i in range(len(self.categories)):
            self.labels[i].setText(_translate("Dialog", str(self.categories[i])))
            self.boxes[i].setItemText(0, _translate("Dialog", "Любой"))
            for j in range(1, len(self.values[i]) + 1):
                self.boxes[i].setItemText(j, _translate("Dialog", str(self.values[i][j - 1])))

        for i in range(len(self.categories)):
            self.combobox_choose_cat.setItemText(i, _translate("Dialog", str(self.categories[i])))
        self.label_last.setText(_translate("Dialog", "Выберите параметр:"))

        self.pushButton.setText(_translate("Dialog", "Найти"))
