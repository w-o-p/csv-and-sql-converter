# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'table_choose.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog, message):
        self.message = message

        Dialog.setObjectName("Dialog")
        Dialog.resize(373, 121)
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(92, 10, 189, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label_warning = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_warning.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_warning)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        if self.message:
            self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">"
                                                    "{}</p></body></html>".format(self.message)))
        else:
            self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">"
                                                    "Какую таблицу вы хотите открыть?</p></body></html>"))
        self.pushButton.setText(_translate("Dialog", "Открыть"))
        # self.label_warning.setText(_translate("Dialog", "Не удалось открыть таблицу"))