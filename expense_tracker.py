from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from datetime import datetime
import sqlite3 as db
import pandas as pd
import sys


def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(300, 300, 300, 300)
    win.setWindowTitle('Expense Tracker')

    weekly_expense_button = QtWidgets.QPushButton(win)
    weekly_expense_button.setText('Weekly Expenses')
    weekly_expense_button.setGeometry(0, 0, 130, 50)

    win.show()
    sys.exit(app.exec_())


window()
