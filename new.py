# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'flag.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import sys
import csv
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from file1 import Example
from tbl_choose import Ui_Dialog


class Choose(Ui_Dialog, QMainWindow):
    def __init__(self, name='', open=False, table='', label=''):
        super().__init__()
        self.file_name = name
        self.open = open
        self.message = ''
        if label == 'conv':
            self.message = 'Назовите таблицу'
        else:
            self.label_warnings = label
        self.table = table
        self.setupUi(self, self.message)
        if not self.message:
            self.pushButton.clicked.connect(self.open_file)
        else:
            self.pushButton.clicked.connect(self.get_str)

    def open_file(self):
        try:
            # Подключение к БД
            con = sqlite3.connect(self.file_name)
            cur = con.cursor()
            result = cur.execute('''SELECT * FROM {}'''.format(self.lineEdit.text())).fetchall()
            self.open = True
            self.table = self.lineEdit.text()
            if self.label_warnings:
                self.label_warnings.setText('Файл успешно открыт')
            con.close()
            self.close()
        except Exception:
            self.label_warning.setText("Не удалось открыть таблицу")

    def get_str(self):
        self.table = self.lineEdit.text()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Choose()
    ex.show()
    sys.exit(app.exec_())