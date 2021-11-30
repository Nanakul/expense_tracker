import sqlite3
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from datetime import datetime
import sqlite3 as db
import pandas as pd
import sys

# 1 -- Entering expenses == DONE
# 2 -- Return all expenses == DONE
# 3 -- Return all expenses from current date to specified date == DONE
# 4 -- Return all expenses between two specified dates

# Connect the database
connect = db.connect('Expenses.db')
cursor = connect.cursor()
# cursor.execute("""CREATE TABLE Expenses4 (
#                 item VARCHAR,
#                 date VARCHAR,
#                 price VARCHAR
#                 )""")
connect.commit()


def new_expense():
    item = input('What did you purchase? ')
    date_purchased = input('What day did you make the purchase? Format: MM/DD/YYYY ')
    item_price = input('How much did this cost? ')

    connect.execute('INSERT INTO Expenses VALUES (?, ?, ?)',
                    (str(item), str(date_purchased), str(item_price)))
    connect.commit()


def display_all_expenses():
    cursor.execute('SELECT * FROM Expenses')
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    connect.commit()


def display_expense_to_current():
    cursor.execute('SELECT strftime("%m/%d/%Y", "now")')
    cursor.execute('SELECT * FROM Expenses WHERE date < strftime("%m/%d/%Y", "now")')
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    connect.commit()


def expense_between_range():
    date1 = input('Enter a date to get expense range from. Format: MM/DD/YYYY ')
    date2 = input('Enter the end date. Format: MM/DD/YYYY ')
    cursor.execute('SELECT strftime("%m/%d/%Y", "now")')
    cursor.execute('SELECT * FROM Expenses WHERE date BETWEEN (?) and (?)', (str(date1), str(date2)))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    connect.commit()


# new_expense()
# display_all_expenses()
# display_expense_to_current()
expense_between_range()

# class MyWindow(QMainWindow):
#     def __init__(self):
#         super(MyWindow, self).__init__()
#         self.label = QtWidgets.QLabel(self)
#         self.weekly_expense_button = QtWidgets.QPushButton(self)
#         self.setGeometry(300, 300, 300, 300)
#         self.setWindowTitle('Expense Tracker')
#         self.initialize_ui()
#
#     def initialize_ui(self):
#         self.label.setText('Not clicked.')
#         self.label.move(50, 50)
#
#         self.weekly_expense_button.setText('Weekly Expenses')
#         self.weekly_expense_button.setGeometry(0, 0, 130, 50)
#         self.weekly_expense_button.clicked.connect(self.weekly_expense_button_click)
#
#     def weekly_expense_button_click(self):
#         self.label.setText('You have clicked the button!')
#         self.update()
#
#     def update(self):
#         self.label.adjustSize()
#
#
# def window():
#     app = QApplication(sys.argv)
#     win = MyWindow()
#     win.show()
#     sys.exit(app.exec_())


# window()

if __name__ == '__main__':
    pass
