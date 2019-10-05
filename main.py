import sys

import csv
import time
import datetime
from random import randint
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QTreeWidgetItem, QTableWidgetItem
from PyQt5 import QtCore, QtGui
from main_ui import Ui_Main
from new_task import Ui_newTaskDialog
from names_list import Ui_NamesList
from edit_name import Ui_EditName

_translate = QtCore.QCoreApplication.translate


class Todo(QMainWindow, Ui_Main):
    def __init__(self, parent=None):
        super(Todo, self).__init__(parent=parent)
        self.setupUi(self)
        self.show_todo_list()
        self.newTask.clicked.connect(self.new_task)
        self.treeWidget.itemDoubleClicked.connect(self.edit_task)
        self.pushButton.clicked.connect(self.workers)
        self.pushButton_2.clicked.connect(self.categories)

    def workers(self):
        workers_list = Names(self, table='worker')
        workers_list.setWindowTitle(_translate("newTaskDialog", "Workers"))
        workers_list.exec()
        self.show_todo_list()

    def categories(self):
        workers_list = Names(self, table='category')
        workers_list.setWindowTitle(_translate("newTaskDialog", "Categories"))
        workers_list.exec()
        self.show_todo_list()

    def show_todo_list(self):
        self.treeWidget.clear()
        with sqlite3.connect('todotool') as con:
            data = con.execute('''
                SELECT 
                    super,
                    t.id, 
                    date,
                    header,
                    c.name,
                    w.name,
                    status, 
                    importance
                from task as t left join worker as w on t.worker = w.id left join category as c on t.category = c.id
                ''').fetchall()
            data = list(map(lambda row: list(row) if row[0] else [0] + list(row)[1:], data))
        data.sort()

        tasks_dict = {}
        top_index = 0
        for row in data:
            if not row[0]:
                created_item = QTreeWidgetItem(self.treeWidget)
                selected_item = self.treeWidget.topLevelItem(top_index)
                tasks_dict[row[1]] = [created_item, selected_item, 0]
                self.show_task(selected_item, row)
                top_index += 1
            else:
                parent_item_created, parent_item_selected, childs = tasks_dict[row[0]]
                created_item = QTreeWidgetItem(parent_item_created)
                selected_item = parent_item_selected.child(childs)
                tasks_dict[row[0]][2] += 1
                tasks_dict[row[1]] = [created_item, selected_item, 0]
                self.show_task(selected_item, row)

    def show_task(self, selected_item, row):
        for j, col in enumerate(row[1:-1]):
            str_form = str(col)
            if col is None:
                str_form = ''
            if j == 5:
                str_form = 'closed' if col else 'open'
            selected_item.setText(j, _translate("Main", str_form))
        if row[-1] == 2:
            brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
            brush.setStyle(QtCore.Qt.SolidPattern)
            selected_item.setBackground(0, brush)
        if row[-1] == 3:
            brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
            brush.setStyle(QtCore.Qt.SolidPattern)
            selected_item.setBackground(0, brush)

    def new_task(self):
        new_task_dialog = NewTaskDialog(self)
        if new_task_dialog.exec():
            with sqlite3.connect('todotool') as con:
                category_id = con.execute(f'''
                    select id from category where name="{new_task_dialog.comboBox.currentText()}"
                    ''').fetchall()[0][0]
            columns = ['header', 'category', 'Importance', 'date', 'status']
            vals = [
                f'"{new_task_dialog.lineEdit.text()}"',
                str(category_id),
                new_task_dialog.comboBox_2.currentText(),
                f'"{new_task_dialog.dateEdit.text()}"',
                f'"{0 if new_task_dialog.comboBox_3.currentText() == "Open" else 1 }"'
            ]
            if new_task_dialog.lineEdit_2.text():
                columns.append('super')
                vals.append(new_task_dialog.lineEdit_2.text())
            if new_task_dialog.comboBox_4.currentText() != 'None':
                columns.append('worker')
                with sqlite3.connect('todotool') as con:
                    worker_id = con.execute(f'''
                        select id from worker where name="{new_task_dialog.comboBox_4.currentText()}"
                        ''').fetchall()[0][0]
                print(worker_id)
                vals.append(str(worker_id))

            with sqlite3.connect('todotool') as con:
                con.execute(f'''
                    Insert into task ({', '.join(columns)})
                    values ({', '.join(vals)})
                ''')
            self.show_todo_list()

    def edit_task(self, item, column_no):
        new_task_dialog = NewTaskDialog(self, task_id=int(item.text(0)))
        new_task_dialog.setWindowTitle(_translate("newTaskDialog", "Edit Task"))
        if new_task_dialog.exec():
            if not new_task_dialog.deleted:
                with sqlite3.connect('todotool') as con:
                    category_id = con.execute(f'''
                        select id from category where name="{new_task_dialog.comboBox.currentText()}"
                        ''').fetchall()[0][0]
                columns = ['header', 'category', 'Importance', 'date', 'status']
                vals = [
                    f'"{new_task_dialog.lineEdit.text()}"',
                    str(category_id),
                    new_task_dialog.comboBox_2.currentText(),
                    f'"{new_task_dialog.dateEdit.text()}"',
                    f'"{0 if new_task_dialog.comboBox_3.currentText() == "Open" else 1 }"'
                ]
                if new_task_dialog.lineEdit_2.text():
                    columns.append('super')
                    vals.append(new_task_dialog.lineEdit_2.text())
                if new_task_dialog.comboBox_4.currentText() != 'None':
                    columns.append('worker')
                    with sqlite3.connect('todotool') as con:
                        worker_id = con.execute(f'''
                            select id from worker where name="{new_task_dialog.comboBox_4.currentText()}"
                            ''').fetchall()[0][0]
                    vals.append(str(worker_id))

                with sqlite3.connect('todotool') as con:
                    con.execute(f'''
                        UPDATE task 
                        set {", ".join([columns[i] + "=" + vals[i] for i in range(len(vals))])}
                        where id = {item.text(0)}
                    ''')
            else:
                with sqlite3.connect('todotool') as con:
                    con.execute(f'''
                        update task
                        set super = NULL
                        where super = {new_task_dialog.task_id}
                    ''')
            self.show_todo_list()


class NewTaskDialog(QDialog, Ui_newTaskDialog):
    def __init__(self, *args,  task_id=-1):
        super().__init__(*args)
        self.setupUi(self)
        self.task_id = task_id

        self.pushButton_3.setVisible(False)
        categories = self.get_categories()
        for category in categories:
            self.comboBox.addItem(category)

        workers = self.get_workers()
        for worker in workers:
            self.comboBox_4.addItem(worker)

        self.deleted = False

        if task_id > -1:
            self.pushButton_3.setVisible(True)
            self.pushButton_3.setEnabled(True)
            self.show_initial_vals()

        self.pushButton_2.clicked.connect(self.check_data)
        self.pushButton.clicked.connect(self.reject)
        self.pushButton_3.clicked.connect(self.delete)

    def delete(self):
        with sqlite3.connect('todotool') as con:
            con.execute(f'''
                Delete from task
                where id = {self.task_id}
            ''')
        self.deleted = True
        self.accept()

    def show_initial_vals(self):
        with sqlite3.connect('todotool') as con:
            data = con.execute(f'''
                SELECT 
                    header,
                    c.name,
                    importance,
                    super,
                    w.name,
                    date,
                    status
                from task as t left join worker as w on t.worker = w.id left join category as c on t.category = c.id
                where t.id = {self.task_id}
                ''').fetchall()[0]
        self.lineEdit.setText(data[0])
        self.comboBox.setCurrentText(data[1])
        self.comboBox_2.setCurrentText(str(data[2]))
        if data[3]:
            self.lineEdit_2.setText(str(data[3]))
        if data[4]:
            self.comboBox_4.setCurrentText(data[4])
        self.dateEdit.setDate(QtCore.QDate.fromString(data[5], "dd.MM.yyyy"))
        self.comboBox_3.setCurrentText("Closed" if data[6] else "Open")

    def check_data(self):
        if self.check_super_id():
            if self.check_header():
                return self.accept()

    def check_super_id(self):
        if self.lineEdit_2.text():
            if self.lineEdit_2.text().isdigit():
                with sqlite3.connect('todotool') as con:
                    res = con.execute(f'''
                        select * from task where id = {self.lineEdit_2.text()}
                    ''').fetchall()
                if len(res) == 1:
                    return True
                else:
                    self.label_6.setText("The id of super task is incorrect")
                    return False
            else:
                self.label_6.setText("The id of super task must be a number")
                return False
        else:
            return True

    def check_header(self):
        if self.lineEdit.text():
            with sqlite3.connect('todotool') as con:
                res = con.execute(f'''
                    select * from task where header = "{self.lineEdit.text()}"
                ''').fetchall()
            if self.task_id == -1:
                if len(res) > 0:
                    self.label_6.setText("The task with such header already exists")
                    return False
                else:
                    return True
            else:
                if len(res) == 0 or (len(res) == 1 and res[0][0] == self.task_id):
                    return True
                else:
                    self.label_6.setText("The task with such header already exists")
                    return False
        else:
            self.label_6.setText("Header cannot be empty")
            return False

    def get_categories(self):
        with sqlite3.connect('todotool') as con:
            data = con.execute('''
                SELECT 
                    name
                from category
                ''').fetchall()
            data = [d[0] for d in data]
        return data

    def get_workers(self):
        with sqlite3.connect('todotool') as con:
            data = con.execute('''
                SELECT 
                    name
                from worker
                ''').fetchall()
            data = [d[0] for d in data]
        return data


class Names(QDialog, Ui_NamesList):
    def __init__(self, *args, table="worker"):
        super().__init__(*args)
        self.setupUi(self)
        self.table = table
        self.show_list()
        self.pushButton_2.clicked.connect(self.new_name)
        self.pushButton.clicked.connect(self.reject)
        self.tableWidget.itemDoubleClicked.connect(self.edit_task)

    def new_name(self):
        new_name_dialog = EditName(self, table=self.table)
        new_name_dialog.setWindowTitle(_translate("newTaskDialog", "New " + self.table))
        if new_name_dialog.exec():
            with sqlite3.connect('todotool') as con:
                con.execute(f'''
                    Insert into {self.table} (name)
                    values ("{new_name_dialog.lineEdit.text().strip()}")
                ''')
            self.show_list()

    def show_list(self):
        self.tableWidget.clear()
        with sqlite3.connect('todotool') as con:
            data = con.execute(f'''
                SELECT id, name
                from {self.table}
            ''').fetchall()
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(len(data))

        item = QTableWidgetItem()
        item.setText(_translate("NamesList", "name"))
        self.tableWidget.setHorizontalHeaderItem(0, item)
        for i, n in enumerate(data):
            item = QTableWidgetItem()
            item.setText(_translate("NamesList", str(n[0])))
            self.tableWidget.setVerticalHeaderItem(i, item)
            item = QTableWidgetItem()
            item.setText(_translate("NamesList", str(n[1])))
            self.tableWidget.setItem(i, 0, item)

    def edit_task(self, item):
        name_id = self.tableWidget.verticalHeaderItem(item.row()).text()
        edit_name_dialog = EditName(self, table=self.table, name_id=int(name_id))
        edit_name_dialog.setWindowTitle(_translate("newTaskDialog", "Edit "+self.table))

        if edit_name_dialog.exec():
            pass
            if not edit_name_dialog.deleted:
                with sqlite3.connect('todotool') as con:
                    con.execute(f'''
                        UPDATE {self.table}
                        set name = "{edit_name_dialog.lineEdit.text().strip()}"
                        where id = {name_id}
                    ''')
            else:
                with sqlite3.connect('todotool') as con:
                    con.execute(f'''
                        update task
                        set {self.table} = NULL
                        where {self.table} = {edit_name_dialog.name_id}
                    ''')
            self.show_list()


class EditName(QDialog, Ui_EditName):
    def __init__(self, *args, table="worker", name_id=-1):
        super().__init__(*args)
        self.setupUi(self)
        self.name_id = name_id
        self.table = table

        self.pushButton_3.setVisible(False)
        self.deleted = False

        if name_id > -1:
            self.pushButton_3.setVisible(True)
            self.pushButton_3.setEnabled(True)
            self.show_initial_val()

        self.pushButton_2.clicked.connect(self.check_data)
        self.pushButton.clicked.connect(self.reject)
        self.pushButton_3.clicked.connect(self.delete)

    def show_initial_val(self):
        with sqlite3.connect('todotool') as con:
            name = con.execute(f'''
                select name from {self.table}
                where id = {self.name_id}
            ''').fetchall()[0][0]
        self.lineEdit.setText(name)

    def check_data(self):
        if self.check_name():
            return self.accept()

    def check_name(self):
        if not self.lineEdit.text().strip():
            self.label_2.setText("Name cannot be empty")
            return False
        with sqlite3.connect('todotool') as con:
            res = con.execute(f'''
                select * from {self.table}
                where name = "{self.lineEdit.text()}"
            ''').fetchall()
        if self.name_id == -1:
            if len(res) == 0:
                return True
            else:
                self.label_2.setText("Such name already exists")
                return False
        else:
            if len(res) == 0 or (len(res) == 1 and res[0][0] == self.name_id):
                return True
            else:
                self.label_2.setText("Such name already exists")
                return False

    def delete(self):
        with sqlite3.connect('todotool') as con:
            con.execute(f'''
                   Delete from {self.table}
                   where id = {self.name_id}
               ''')
        self.deleted = True
        self.accept()


def main():
    app = QApplication(sys.argv)
    wind = Todo()
    wind.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
