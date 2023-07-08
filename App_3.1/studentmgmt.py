from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QLineEdit, QPushButton, \
    QGridLayout, QMainWindow, QTableWidget, QTableWidgetItem
from PyQt6.QtGui import QAction
import sqlite3

import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Management System")

        file_menu_item = self.menuBar().addMenu("&File")
        help_menu_item = self.menuBar().addMenu("&Help")

        add_student_action = QAction("Add Student",self)
        file_menu_item.addAction(add_student_action)

        add_help_action = QAction("About",self)
        help_menu_item.addAction(add_help_action)

        self.table = QTableWidget()
        self.table.setColumnCount(int(4))
        self.table.setHorizontalHeaderLabels(("ID","Name","Course","Mobile"))
        self.setCentralWidget(self.table)

    def load_data(self):
        connection = sqlite3.connect("database.db")
        result = connection.execute("SELECT * FROM students")
        self.table.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.table.insertRow(row_number)
            for column_number,data in enumerate(row_data):
                self.table.setItem(row_number,column_number, QTableWidgetItem(str(data)))
        connection.close()


app = QApplication(sys.argv)
stud_magmt = MainWindow()
stud_magmt.show()
stud_magmt.load_data()
sys.exit(app.exec())

