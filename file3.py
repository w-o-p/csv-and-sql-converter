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
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
from graph_table import Ui_Table


class Tabl(Ui_Table, QMainWindow):
    def __init__(self, name='', type='', table=''):
        super().__init__()
        self.file_type = type
        self.file_name = name
        self.categories = []
        self.rows = []
        self.table = table
        self.modified = {}
        self.con = ''
        self.val_changed = []
        self.clicked_item = ''
        self.edited = False
        # self.item_can_be_deleted = ''
        if self.file_type == 'csv':
            self.open_file_csv()
        elif self.file_type == 'sqlite' or self.file_type == 'db' or self.file_type == 'db3':
            self.open_file_sql()
        self.setupUi_table(self, self.categories, self.rows)

        self.tableWidget.itemChanged.connect(self.item_changed)
        self.tableWidget.itemClicked.connect(self.set_item)
        self.pushButton_save.clicked.connect(self.save_results)
        self.pushButton_delete.clicked.connect(self.delete)

    def open_file_csv(self):
        with open(self.file_name, encoding="utf8") as csvfile:
            reader = csv.reader(csvfile, delimiter=';', quotechar='"')
            for index, row in enumerate(reader):
                if index == 0:
                    self.categories = row
                else:
                    self.rows.append(row)

    def open_file_sql(self):
        con = sqlite3.connect(self.file_name)
        cur = con.cursor()
        result = cur.execute('''SELECT * FROM {}'''.format(self.table)).fetchall()
        for i in range(len(cur.description)):
            self.categories.append(cur.description[i][0])
        for elem in result:
            self.rows.append(list(elem))
        con.close()

    def item_changed(self, item):
        self.modified[self.categories[item.column()]] = item.text()

        for i in range(len(self.categories)):
            self.val_changed.append(self.rows[self.clicked_item.row()][i])

        for i in range(len(self.val_changed)):
            if isinstance(self.val_changed[i], str):
                self.val_changed[i] = '"' + self.val_changed[i] + '"'

        self.tableWidget.setEnabled(False)
        self.edited = True

    def save_results(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Question)

        msg.setWindowTitle("Save")
        msg.setText("Вы уверены, что хотите сохранить изменения?")

        yesButton = msg.addButton('Да', QMessageBox.AcceptRole)
        msg.addButton('Отмена', QMessageBox.RejectRole)

        msg.exec()
        if msg.clickedButton() == yesButton:
            try:
                if self.modified:
                    self.con = sqlite3.connect(self.file_name)
                    cur = self.con.cursor()
                    que = "UPDATE {} SET\n".format(self.table)
                    for key in self.modified.keys():
                        que += "{}='{}'\n".format(key, self.modified.get(key))
                    que += 'WHERE'
                    params = []
                    for i in range(len(self.categories)):
                        params.append(' {} = {} '.format(str(self.categories[i]), str(self.val_changed[i])))
                    params = 'and'.join(params)
                    que += params
                    cur.execute(que)
                    self.con.commit()
                    self.modified.clear()
                    self.tableWidget.setEnabled(True)
                    #self.edited = True
            except Exception:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)

                msg.setWindowTitle("Error")
                msg.setText("Произошла ошибка")

                msg.addButton('Ок', QMessageBox.RejectRole)

                msg.exec()

    def delete(self):
        if not self.edited:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Question)

            msg.setWindowTitle("Delete")
            msg.setText("Вы уверены, что хотите удалить эту строку?")

            yesButton = msg.addButton('Да', QMessageBox.AcceptRole)
            msg.addButton('Отмена', QMessageBox.RejectRole)

            msg.exec()
            if msg.clickedButton() == yesButton:
                try:
                    if self.file_type == 'csv' or not self.clicked_item:
                        raise Exception

                    for i in range(len(self.categories)):
                        self.val_changed.append(self.rows[self.clicked_item.row()][i])

                    for i in range(len(self.val_changed)):
                        if isinstance(self.val_changed[i], str):
                            self.val_changed[i] = '"' + self.val_changed[i] + '"'

                    con = sqlite3.connect(self.file_name)
                    cur = con.cursor()

                    que = 'DELETE from {}\n'.format(self.table)
                    que += 'WHERE'
                    params = []
                    for i in range(len(self.categories)):
                        params.append(' {} = {} '.format(str(self.categories[i]), str(self.val_changed[i])))
                    params = 'and'.join(params)
                    que += params

                    cur.execute(que)
                    con.commit()
                    self.val_changed = []
                    self.close()
                except Exception:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)

                    msg.setWindowTitle("Error")
                    msg.setText("Произошла ошибка")

                    msg.addButton('Ок', QMessageBox.RejectRole)

                    msg.exec()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Question)

            msg.setWindowTitle("Warning")
            msg.setInformativeText("Чтобы удалить строку нужно заново открыть это окно")
            msg.setText("Вы хотите выйти?")

            yesButton = msg.addButton('Да', QMessageBox.AcceptRole)
            msg.addButton('Отмена', QMessageBox.RejectRole)

            msg.exec()
            if msg.clickedButton() == yesButton:
                self.close()

    def set_item(self, item):
        self.clicked_item = item


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Tabl()
    ex.show()
    sys.exit(app.exec_())
